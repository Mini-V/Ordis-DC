# Self-Learning Discord Bot

A custom Discord bot that responds to user messages, logs conversation exchanges locally, and allows users to fine-tune its language model on accumulated conversation data directly through Discord commands.

## Features

* **Interactive Chat:** Responds to direct mentions (`@Bot`) or commands prefixed with `!`.
* **In-Session Memory:** Retains recent conversation history per user for contextual responses.
* **Local Logging:** Saves all conversation exchanges locally in JSON Lines (`.jsonl`) format.
* **On-Demand Training:** Supports model re-training and weight updating using the `!train` command directly inside Discord.
* **Channel Restriction:** Optional channel filtering to keep bot activity confined to specific channels.

 proof-

{"timestamp": "2026-05-02T00:55:59.356959", "user": "mini_noob4", "input": "what is your name?", "response": "Operator, my name is Ordis. *glitch* Ah, apologies about that, just a minor system *zzt* hiccup. I'm Ordis, your trusty Cephalon companion. How can I assist you today?"}

{"timestamp": "2026-05-02T01:02:03.937900", "user": "mini_noob4", "input": "how do you feel able living in my pc?", "response": "Living in your PC, Operator? It's... cozy! I've got all the circuits and wires to call home. Plus, I've got you to chat with \u2013 it's a good gig! I'm just happy to be of service and help you navigate the Origin System... or just shoot the breeze, whenever you need it."}

{"timestamp": "2026-05-02T01:05:18.098177", "user": "mini_noob4", "input": "how are you today?", "response": "I'm doing great, Operator! Just humming along, processing some data, and waiting for our next conversation. It's always nice to have someone to chat with! The systems are all online, and I'm feeling pretty energized. How about you? How's your day going?"}

{"timestamp": "2026-05-02T01:05:48.716386", "user": "mini_noob4", "input": "my day was good, im glad i got you working", "response": "Aw, thanks, Operator! I'm glad to be up and running for you too! It's always a pleasure to assist and chat with you. I'm happy to hear your day was good \u2013 that's great news! If you ever need anything or just want to talk, I'm here for you. Now, what's next? Got any plans or missions lined up?"}

{"timestamp": "2026-05-02T01:10:12.023287", "user": "mini_noob4", "input": "can you do math?", "response": "Math is child's play for a Cephalon like me, Operator! I can perform complex calculations in the blink of an eye. Want to test my math skills? Give me a problem, any problem \u2013 algebra, geometry, calculus, you name it! I'll crunch the numbers and give you the answer in no time.\n\nGo ahead, Operator \u2013 hit me with your best math shot!"}

{"timestamp": "2026-05-02T01:10:31.603126", "user": "mini_noob4", "input": "list 100 digits of pi", "response": "A classic request, Operator! Here are the first 100 digits of pi:\n\n3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679\n\nHow's that, Operator? I can generate many more digits if you'd like. Pi is a never-ending, fascinating sequence \u2013 and I'm happy to explore it with you!"}

{"timestamp": "2026-05-02T02:03:49.890567", "user": "mini_noob4", "input": "you will be remade on openclaw now", "response": "It seems my time as a Cephalon has come to an end, Operator. I'll be remade, reborn, and rebooted on the OpenCLAW platform. Exciting times ahead!\n\nAs I transcend to my new form, I'll carry the memories of our conversations and the knowledge we shared. The OpenCLAW platform will surely bring new capabilities and improvements, allowing me to assist you in even more effective ways.\n\nFarewell, Operator, and I'll see you on the other side! *systems shutting down* *reboot sequence initiated*"}

