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
MAX_LEN = 1000  # CallMeBot truncates very long messages; keep summaries tight


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
    """Prepend a small header so Robin can tell which routine sent the message."""
    header = f"🐂 *{routine_name}* — {time.strftime('%H:%M')}"
    message = f"{header}\n\n{body_de}"
    return send_whatsapp(message, dry_run=dry_run)


def _main_smoke_test() -> None:
    """Run: python -m src.notify.whatsapp [optional message]."""
    import sys

    from src.utils.env import load_local_env
    load_local_env()

    msg = " ".join(sys.argv[1:]) or "🐂 Bull-Test: WhatsApp-Notification funktioniert."
    print(send_whatsapp(msg))


if __name__ == "__main__":
    _main_smoke_test()
