"""CallMeBot WhatsApp notifier.

CallMeBot is a free service for sending WhatsApp messages to your own number via a
simple HTTP GET. To activate (one-time, manual):
    1. Add the number +34 644 51 90 30 to your contacts.
    2. Send "I allow callmebot to send me messages to my phone" via WhatsApp.
    3. Receive your personal API key in the reply.
    4. Set env vars: CALLMEBOT_API_KEY, WHATSAPP_PHONE (e.g. 491701234567, no '+').

API docs: https://www.callmebot.com/blog/free-api-whatsapp-messages/
Rate limit: ~1 message per ~30s. Don't spam.
"""
from __future__ import annotations

import os
import time
from urllib.parse import quote_plus

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential


API_URL = "https://api.callmebot.com/whatsapp.php"
MAX_LEN = 1000  # CallMeBot's documented per-call ceiling; we send below this
SAFE_PART_LEN = 700  # Empirical: CallMeBot starts cutting mid-message above ~700-800
                     # chars even though the docs say 1000. Always split below this.
INTER_PART_SLEEP = 35  # CallMeBot rate-limit: ~1 message / 30s. Wait between parts.


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=20))
def send_whatsapp(message: str, *, dry_run: bool = False) -> str:
    """Send a WhatsApp message via CallMeBot.

    Args:
        message: The text body. Keep under 1000 chars. Markdown is NOT rendered — WhatsApp
                 supports limited formatting (*bold*, _italic_, ~strikethrough~).
        dry_run: If True, prints message to stdout instead of sending.

    Returns:
        The HTTP response body (CallMeBot returns a short status string).
    """
    if dry_run:
        print(f"[DRY-RUN WhatsApp]\n{message}")
        return "dry-run"

    api_key = os.environ.get("CALLMEBOT_API_KEY")
    phone = os.environ.get("WHATSAPP_PHONE")
    if not api_key or not phone:
        raise RuntimeError(
            "CALLMEBOT_API_KEY and WHATSAPP_PHONE env vars must be set. "
            "See src/notify/whatsapp.py docstring for one-time setup."
        )

    body = message[:MAX_LEN]
    params = {
        "phone": phone,
        "text": body,
        "apikey": api_key,
    }
    # Build query manually to ensure consistent encoding of newlines (\n -> %0A)
    query = "&".join(f"{k}={quote_plus(str(v))}" for k, v in params.items())
    url = f"{API_URL}?{query}"

    with httpx.Client(timeout=30.0) as client:
        response = client.get(url)
        response.raise_for_status()
        return response.text


def send_routine_summary(
    routine_name: str,
    body_de: str,
    *,
    dry_run: bool = False,
) -> str:
    """Prepend a small header so Robin can tell which routine sent the message.

    For a single short message only. If `body_de` may exceed ~700 chars,
    use `send_long_routine_message` instead — CallMeBot cuts above that.
    """
    header = f"🐂 *{routine_name}* — {time.strftime('%H:%M')}"
    message = f"{header}\n\n{body_de}"
    return send_whatsapp(message, dry_run=dry_run)


def _split_on_blank_lines(body: str, max_chars: int) -> list[str]:
    """Split a long body into chunks of <= max_chars, breaking on blank-line
    paragraph boundaries (`\\n\\n`). Falls back to hard splits only if a single
    paragraph is itself longer than max_chars (rare for our briefs).
    """
    paragraphs = body.split("\n\n")
    chunks: list[str] = []
    current = ""
    for p in paragraphs:
        sep = "\n\n" if current else ""
        if len(current) + len(sep) + len(p) <= max_chars:
            current = current + sep + p
            continue
        if current:
            chunks.append(current)
            current = ""
        # Paragraph alone may still exceed limit — hard-split as last resort.
        while len(p) > max_chars:
            chunks.append(p[:max_chars])
            p = p[max_chars:]
        current = p
    if current:
        chunks.append(current)
    return chunks


def send_long_routine_message(
    routine_name: str,
    body_de: str,
    *,
    dry_run: bool = False,
    safe_part_len: int = SAFE_PART_LEN,
    inter_part_sleep: int = INTER_PART_SLEEP,
) -> list[str]:
    """Send a German routine brief, splitting into multiple WhatsApp messages
    when the body would exceed CallMeBot's effective truncation window.

    - Single-part path: same header as `send_routine_summary`.
    - Multi-part path: each part gets a "🐂 *<routine>* (N/M) — HH:MM" header
      so Robin can re-stitch them in order. Sleeps `inter_part_sleep` seconds
      between parts to respect CallMeBot's ~1 msg / 30 s rate limit.

    Returns the list of CallMeBot response bodies, one per part.
    """
    timestamp = time.strftime("%H:%M")
    # Reserve room for the longest possible header. Multi-part header pattern:
    #   "🐂 *<routine>* (N/M) — HH:MM\n\n"
    # max(N) and max(M) bounded by 9 each (we never expect >9 parts).
    header_budget = len(f"🐂 *{routine_name}* (9/9) — {timestamp}\n\n")
    chunk_budget = max(50, safe_part_len - header_budget)

    chunks = _split_on_blank_lines(body_de, chunk_budget)
    total = len(chunks)

    responses: list[str] = []
    for idx, chunk in enumerate(chunks, start=1):
        if total == 1:
            header = f"🐂 *{routine_name}* — {timestamp}"
        else:
            header = f"🐂 *{routine_name}* ({idx}/{total}) — {timestamp}"
        message = f"{header}\n\n{chunk}"
        responses.append(send_whatsapp(message, dry_run=dry_run))
        if idx < total and not dry_run:
            time.sleep(inter_part_sleep)
    return responses


def _main_smoke_test() -> None:
    """Run: python -m src.notify.whatsapp [optional message]."""
    import sys

    from src.utils.env import load_local_env
    load_local_env()

    msg = " ".join(sys.argv[1:]) or "🐂 Bull-Test: WhatsApp-Notification funktioniert."
    print(send_whatsapp(msg))


if __name__ == "__main__":
    _main_smoke_test()
