# SETUP — Manuelle Schritte für Robin

Diese Schritte musst du selbst machen, weil sie Accounts/Auth/Hardware betreffen, die ich nicht für dich erledigen kann. Reihenfolge ist wichtig.

---

## Phase 0 — Local Smoke Test (1 Stunde, optional aber empfohlen)

### 0.1 Python-Umgebung anlegen
```powershell
cd "D:\Claude Trading Bot"
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
```

### 0.2 Alpaca Paper Account
1. Geh auf https://alpaca.markets/ → "Sign up" → "Paper Trading" (kostenlos, keine Verifikation nötig)
2. Im Dashboard rechts: **Generate New Key** → **Key** und **Secret** sofort kopieren (Secret siehst du nur einmal!)
3. In `D:\Claude Trading Bot\.env` (kopieren von `.env.example`):
   ```
   ALPACA_API_KEY_ID=PKxxxxxxxxxxxx
   ALPACA_API_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ALPACA_BASE_URL=https://paper-api.alpaca.markets
   ACTIVE_BROKER=alpaca
   ```
4. Test:
   ```powershell
   python -m src.brokers.alpaca
   ```
   → Sollte deinen Paper-Account zeigen (default ~$100k).

### 0.3 Gemini API Key (Primär-Recherche, kostenlos)
1. Geh auf https://aistudio.google.com/apikey
2. Mit Google-Account einloggen → **Create API Key** → "Create API key in new project" (oder existierendes)
3. Key kopieren — Format: `AIza...`
4. Kein Bezahlmodel hinterlegen nötig. Free Tier: 1500 Requests/Tag Gemini 2.5 Flash mit Search Grounding.
5. In `.env`:
   ```
   GEMINI_API_KEY=AIzaxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
6. Test:
   ```powershell
   python -m src.research.gemini "Latest macro outlook US large-cap tech, 2 sentences"
   ```

### 0.3b Tavily API Key (nur für deep_research, kostenlos)
1. https://tavily.com/ → "Sign up" mit GitHub oder Google
2. Dashboard → **API Keys** → "Create new API key" (kein Bezahlmodel nötig)
3. Format: `tvly-...`. Free Tier: 1000 Requests/Monat (wir nutzen ~50/Monat für Cross-Validation).
4. In `.env`:
   ```
   TAVILY_API_KEY=tvly-xxxxxxxxxxxxx
   ```
5. Test:
   ```powershell
   python -m src.research.tavily "NVDA latest earnings reaction"
   ```

### 0.3c yfinance (keine Anmeldung nötig)
yfinance scraped Yahoo Finance ohne API-Key. Quick-Test:
```powershell
python -m src.research.fundamentals AAPL
```
Sollte Preis, P/E, Margen etc. ausgeben.

### 0.4 CallMeBot WhatsApp aktivieren
1. **Kontakt anlegen** auf deinem Handy: `+34 644 51 90 30` (irgendein Name)
2. WhatsApp öffnen, dem Kontakt schreiben: `I allow callmebot to send me messages to my phone`
3. Antwort kommt nach 1–2 Minuten mit deinem persönlichen `apikey`. **API-Key kopieren.**
4. In `.env`:
   ```
   CALLMEBOT_API_KEY=1234567
   WHATSAPP_PHONE=491701234567
   ```
   ⚠️ Deine Nummer **ohne "+"**, mit Länder-Vorwahl.
5. Test:
   ```powershell
   python -m src.notify.whatsapp "Test von Bull"
   ```
   → Sollte als WhatsApp-Nachricht ankommen. Falls "APIKey not enabled" → 2 Min warten, Aktivierung läuft asynchron.

---

## Phase 1 — GitHub Repo (15 Min)

### 1.1 GitHub CLI authentifiziert?
```powershell
gh auth status
```
Falls nicht → `gh auth login` → Browser-Flow.

### 1.2 Repo erstellen + initialer Push
```powershell
cd "D:\Claude Trading Bot"
git init
git branch -M main
git add .
git status   # ⚠️ KEINE .env in der Liste! Falls doch: STOP, .gitignore prüfen.
git commit -m "feat: initial trading bot scaffold with memory architecture"

gh repo create trading-bot --private --source=. --remote=origin --push
```

### 1.3 Verifizieren
```powershell
gh repo view trading-bot --web
```
→ Browser öffnet sich, du solltest alle Files sehen.

---

## Phase 2 — Claude Cloud Environment (10 Min)

### 2.1 Claude Desktop App
Falls noch nicht installiert: https://claude.ai/download → Windows-Version.
Mit deinem Anthropic-Account einloggen (du brauchst mindestens **Pro** oder besser **Max** für Routines).

### 2.2 Cloud Environment "trading" anlegen
1. Sidebar → **Routines** → **New Routine** → **Remote**
2. Klick auf "Cloud Environments" → **Add**
3. Name: `trading`
4. **Network access:** Full (Bot muss zu Alpaca, Gemini/Google AI, Tavily, Yahoo Finance, CallMeBot, GitHub)
5. **Environment Variables** (genau diese Namen — die Routines erwarten sie):
   ```
   ALPACA_API_KEY_ID         = <dein Alpaca Key>
   ALPACA_API_SECRET_KEY     = <dein Alpaca Secret>
   ALPACA_BASE_URL           = https://paper-api.alpaca.markets
   ACTIVE_BROKER             = alpaca
   GEMINI_API_KEY            = AIza...
   TAVILY_API_KEY            = tvly-...
   CALLMEBOT_API_KEY         = <dein CallMeBot Key>
   WHATSAPP_PHONE            = 491701234567
   GIT_AUTHOR_NAME           = Bull Bot
   GIT_AUTHOR_EMAIL          = bot@trading.local
   ```
6. Speichern.

---

## Phase 3 — Routinen anlegen (30 Min)

Für **jede** der 7 Routinen (`00`, `01`, …, `06`) wiederholst du:

1. Sidebar → **Routines** → **New Routine** → **Remote**
2. **Repository:** `<dein-username>/trading-bot`, Branch: `main`
3. **Cloud Environment:** `trading`
4. **Model:** `claude-opus-4-7`
5. **Cron-Expression** (genau diese, UTC):

   | Routine | Cron (UTC) | Schedule? |
   |---|---|---|
   | `00-strategy-init` | (kein Cron — "Run now" only) | Manuell |
   | `01-pre-market` | `0 13 * * 1-5` | Mo-Fr 14:00 DE |
   | `02-market-open` | `30 14 * * 1-5` | Mo-Fr 15:30 DE |
   | `03-midday` | `30 17 * * 1-5` | Mo-Fr 18:30 DE |
   | `04-pre-close` | `30 20 * * 1-5` | Mo-Fr 21:30 DE |
   | `05-close-summary` | `15 21 * * 1-5` | Mo-Fr 22:15 DE |
   | `06-weekly-review` | `30 21 * * 5` | Freitag 22:30 DE |

6. **Prompt:** Inhalt der entsprechenden Datei aus `routines/<slug>.md` **vollständig** reinkopieren.
7. **Permissions** → **"Allow unrestricted branch pushes"** aktivieren. ⚠️ Wichtig — sonst kann Bot nicht zu `main` pushen.
8. Speichern.

---

## Phase 4 — Initial Strategy Run (15 Min Bot-Arbeit, dann Robin reviewt)

### 4.1 Trigger `00-strategy-init` manuell
- Routines → `00-strategy-init` → **Run now**
- Bot läuft ~5-15 Min (4-6 Gemini-Queries + yfinance-Lookups + 1-2 Tavily-Crosschecks für Macro)
- Du kriegst WhatsApp mit Hinweis "Strategie-Vorschläge fertig"

### 4.2 Review auf GitHub
- Öffne `memory/strategy_candidates.md` im Repo
- Lies die 3 Varianten (A, B, C)
- Schau dir Bulls Empfehlung an

### 4.3 Strategie zementieren
- Öffne `memory/strategy.md` im Repo direkt im GitHub-Web-Editor
- **Ersetze den kompletten Inhalt** mit der gewählten Variante
- Frontmatter so anpassen:
  ```yaml
  ---
  version: 1
  approved: true
  created: 2026-05-11
  last_modified: <heute>
  active_variant: A  # oder B oder C
  ---
  ```
- Commit direkt auf `main` mit Message: `feat: approve strategy variant <A/B/C>`

### 4.4 Verifizieren
- Trigger `01-pre-market` "Run now" → sollte jetzt durchlaufen ohne "abort: strategy not approved"

---

## Phase 5 — Burn-in Beobachtung (Woche 1-2)

- Schau dir **jeden Tag** die WhatsApp-Summaries an
- Lies bei Auffälligkeiten den `memory/daily/<datum>.md` im Repo
- Beobachte `memory/trade_log.md` — sind die Rationale sinnvoll?
- Bei Bugs: Edit das entsprechende `routines/<slug>.md` File auf GitHub direkt, commit → Bot zieht die neue Version automatisch beim nächsten Cron

---

## Phase 6 — IBKR Live Migration (Woche 4+, nur wenn Paper-Performance stimmt)

Siehe `plans/ich-kreire-dich-als-eventual-spring.md` Sektion "Phase 2". Grobe Schritte:

1. IBKR-Konto in DE eröffnen (1-2 Wochen Wartezeit — schon JETZT parallel anstoßen falls du sicher bist)
2. €300 einzahlen
3. Hetzner Cloud CX11 mieten (~4€/Monat), Ubuntu 22.04
4. IB Gateway + IBC (Auto-Re-Login) installieren
5. `src/brokers/ibkr.py` ausimplementieren (Skelett ist da)
6. Cloud Environment um `IBKR_*` Env-Vars erweitern, `ACTIVE_BROKER=ibkr` setzen
7. Erste Live-Trades mit Mini-Sizes (5-10€) testen, dann hochfahren

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Routine schlägt fehl mit "key not found" | Env-Var-Name im Cloud Env stimmt nicht 1:1 mit Code. Prüfen: groß/kleinschreibung, keine Tippfehler. |
| WhatsApp "APIKey not enabled" | CallMeBot-Aktivierung dauert manchmal 5-10 Min. Erneut versuchen. |
| Bot pusht nichts | "Allow unrestricted branch pushes" in jeder Routine nicht aktiviert. |
| `memory/strategy.md` nicht approved | Routine wartet absichtlich. Schritt 4.3 ausführen. |
| Alpaca "forbidden" Error | Vermutlich live-Endpoint statt paper. `ALPACA_BASE_URL` prüfen. |

---

## Sicherheits-Checkliste vor erstem Live-Trade (Phase 2)

- [ ] `.env` lokal NIE committed
- [ ] Cloud Env Variables sind die einzige Quelle für Secrets
- [ ] IBKR-Account hat 2FA aktiv
- [ ] Hetzner-VPS hat SSH-Key-Only (kein Password-Login)
- [ ] Bull testet 2 Wochen erfolgreich auf Paper
- [ ] Alle Hard-Guardrails in CLAUDE.md noch aktuell
- [ ] Erste Live-Trade-Größe: max 10€
