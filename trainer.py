# With Groq, we don't fine-tune locally anymore.
# Conversations are still logged to conversations.jsonl for your records,
# but !train will let you know fine-tuning isn't available with Groq.

def run_training():
    print("ℹ️  Fine-tuning is not available with the Groq backend.")
    print("   Conversations are still being logged to conversations.jsonl.")
    print("   If you want to fine-tune in the future, switch back to a local model.")