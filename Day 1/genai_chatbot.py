import requests
import json

API_KEY = "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"

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