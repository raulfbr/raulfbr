import os

from groq import Groq

client = Groq(
    api_key="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"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Olá, podemos conversar em Portugês?",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)