from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


def save_memory(messages):
    with open("memory.txt", "w") as x:
        x.write(str(messages) + "\n")

def load_memory():
    if os.path.exists("memory.txt"):
        with open("memory.txt", "r") as x:
            content = x.read().strip()
            return eval(content) if content else []
    return []


messages = load_memory()
user_input = input("Write to ChatGPT here:\n")
if not messages:
    messages=[
        {"role": "system", "content": "We are in a story game. There are two characters. There is the user, and there is a bot named John. We are traversing through a story and the user makes up most of the game."},
        {"role": "user", "content": user_input},
    ]
while user_input != "end":
    response = client.chat.completions.create(
        model="gpt-4",

        messages = messages
    )

    resp = response.choices[0].message.content
    messages.append({"role": "system", "content": resp})
    
    print(resp)
    user_input = input("Write to ChatGPT here:\n")
    messages.append({"role": "user", "content": user_input})
save_memory(messages)