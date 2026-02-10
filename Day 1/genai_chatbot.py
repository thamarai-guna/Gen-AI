import requests
import json

API_KEY = "YOUR_API_KEYS"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

while True:
    msg = input("You: ")
    if msg.lower() == "exit":
        break

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": msg}
        ]
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code == 200:
        reply = r.json()["choices"][0]["message"]["content"]
        print("AI:", reply)
    else:

        print("Error:", r.text)
