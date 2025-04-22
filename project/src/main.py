from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()



def save_memory(messages, inventory): #allow for saving the game
    with open("memory.txt", "w") as x:
        x.write(str({"messages": messages, "inventory": inventory}) + "\n")

def load_memory(): #memory loader for current game
    if os.path.exists("memory.txt"):
        with open("memory.txt", "r") as x:
            content = x.read().strip()
            if content:
                data = eval(content)
                return data["messages"], data["inventory"]
    return [], []

messages, inventory = load_memory() #loads memory of game

user_input = input("Write to ChatGPT here:\n")
if not messages:
    messages=[
        {"role": "system", "content": "We are in a story game. There are two characters. There is the user, and there is a bot named John. We are traversing through a story and the user makes up most of the game."},
        {"role": "user", "content": user_input},
    ]
while user_input.lower() != "end": #ability end game whenever

    item_use = ""

    if user_input.lower() == "inventory":   #ability to check inventory
        print(f"inventory: {inventory}")
        

    elif user_input.lower().startswith("take "): #ability to items to inventory 
        item = user_input.lower().strip()[5:]
        inventory.append(item)
        print(f"{item} added to inventory")
        messages.append({"role": "system", "content": f"inventory: {inventory}"})

    elif user_input.lower().startswith("use "):
        item = user_input.lower().strip()[4:]
        if item in inventory:
            print(f"used {item}")
            item_use = "uses" + item
        elif item not in inventory:
            print(item)
            print("not in inventory")

    else: #ability to continue story
        response = client.chat.completions.create(
            model="gpt-4",

            messages = messages
        )

        resp = response.choices[0].message.content
        messages.append({"role": "assistant", "content": resp})
    
        print(resp)
    user_input = input("Write to ChatGPT here:\n")
    messages.append({"role": "user", "content": user_input + item_use})
save_memory(messages, inventory) #saves to game