import discord
import json
import os
from functools import partial
from datetime import datetime
from model import generate_response, reload_model

# ── Config ─────────────────────────────────────────────────────────────────
TOKEN      = "no no no"
CHANNEL_ID =  "no no no"       # Restrict to one channel (int) or None for everywhere
LOG_FILE   = "conversations.jsonl"

# ── Bot setup ──────────────────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Per-user conversation history (in-session memory)
histories = {}

def log_exchange(username, user_input, bot_response):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": username,
        "input": user_input,
        "response": bot_response
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

@client.event
async def on_ready():
    print(f"✓ Logged in as {client.user}")
    print(f"✓ Logging conversations to: {LOG_FILE}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if CHANNEL_ID and message.channel.id != CHANNEL_ID:
        return
    if not (client.user.mentioned_in(message) or message.content.startswith("!")):
        return

    user_input = message.content.replace(f"<@{client.user.id}>", "").strip()
    if user_input.startswith("!"):
        user_input = user_input[1:].strip()
    if not user_input:
        return

    # ── Commands ────────────────────────────────────────────────────────────
    if user_input.lower() in ("help", "?"):
        help_msg = (
            "**🤖 Here's what I can do:**\n\n"
            "**Chat**\n"
            "> `@me <message>` or `!<message>` — talk to me!\n"
            "> I remember the last 6 messages in our conversation.\n\n"
            "**Commands**\n"
            "> `!reset` — clear your conversation history with me\n"
            "> `!stats` — see how many exchanges I've logged\n"
            "> `!train` — fine-tune my brain on all saved conversations\n"
            "> `!help` — show this message\n\n"
            "**How I learn**\n"
            "> Every time we chat, I save the exchange.\n"
            "> When you run `!train`, I update my weights based on those conversations.\n"
            "> The more we talk, the better I get! 🧠"
        )
        await message.channel.send(help_msg)
        return

    if user_input.lower() == "reset":
        histories[message.author.id] = []
        await message.channel.send("🔄 Conversation reset!")
        return

    if user_input.lower() == "train":
        await message.channel.send("🧠 Starting training on saved conversations... this may take a few minutes.")
        try:
            from trainer import run_training
            await client.loop.run_in_executor(None, run_training)
            reload_model()
            await message.channel.send("✅ Training done! I've updated my weights.")
        except Exception as e:
            await message.channel.send(f"❌ Training failed: {e}")
        return

    if user_input.lower() == "stats":
        count = 0
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                count = sum(1 for _ in f)
        await message.channel.send(f"📊 I have **{count}** conversation exchanges logged so far.")
        return

    # ── Normal response (runs in background thread so Discord doesn't DC) ───
    history = histories.get(message.author.id, [])

    async with message.channel.typing():
        loop = client.loop
        fn = partial(generate_response, user_input, history)
        response, history = await loop.run_in_executor(None, fn)

    histories[message.author.id] = history
    log_exchange(str(message.author), user_input, response)

    if len(response) > 1990:
        response = response[:1990] + "..."

    await message.channel.send(response)

client.run(TOKEN)