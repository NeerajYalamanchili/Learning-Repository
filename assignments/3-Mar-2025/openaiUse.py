from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()



dict1 = {"a":"b"}


user_input = input("Write to ChatGPT here:\n")
messages=[
    {"role": "system", "content": "You want to play 20 questions with me. The guesser asks yes or no questions about an object until they guess it and the answerer says yes or no. If the guesser guesses what the thing is correctly within 20 questions he wins."},
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