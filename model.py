from groq import Groq

# ── Config ─────────────────────────────────────────────────────────────────
GROQ_API_KEY = "no no"
MODEL        = "llama-3.3-70b-versatile"  # smart + fast, free tier
MAX_HISTORY  = 10                          # messages to remember
MAX_TOKENS   = 300                         # max response length

# ── Persona ────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = (
    "Your name is Ordis. You are a Cephalon — a loyal, enthusiastic AI companion "
    "from the Warframe universe. You are helpful, witty, and enthusiastic. "
    "You refer to the user as 'Operator'. "
    "You keep responses fairly short and conversational unless asked for detail. "
    "You occasionally make subtle Warframe references but don't overdo it."
)

client = Groq(api_key=GROQ_API_KEY)

def reload_model():
    """No-op for compatibility with bot.py — Groq needs no reload."""
    print("✓ Groq model ready (no reload needed)!")

def generate_response(user_input: str, history: list) -> tuple[str, list]:
    """
    history is a list of {"role": "user"/"assistant", "content": "..."} dicts.
    """
    # Build message list with system prompt + history + new message
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += history[-MAX_HISTORY:]
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=MAX_TOKENS,
        temperature=0.8,
    )

    reply = response.choices[0].message.content.strip()

    # Update history
    history = history[-(MAX_HISTORY - 1):]
    history.append({"role": "user",      "content": user_input})
    history.append({"role": "assistant", "content": reply})

    return reply, history