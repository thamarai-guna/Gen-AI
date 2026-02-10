#import
from openai import OpenAI
#openai router url and api links
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="YOUR_API_KEYS")
#getting an input from user
user_input=input("ask a qustions:")
#role base ai logic
messages=[{
    "role": "system",
    "content": "You are an IT engineer assistant. Answer only IT and computer-related content. If the question is not IT-related, respond with: 'Only IT and computer-related questions are answered. I am an IT engineer.'"
},{"role": "user",
   "content": user_input}]

response=client.chat.completions.create(
    model="openai/gpt-4",
    messages=messages,
    temperature=0,
    max_tokens=150
)
print(response.choices[0].message.content)


