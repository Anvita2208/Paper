import openai

client = openai.OpenAI(api_keys = ("your_api")


completion = client.chat.completions.create(
    model="gpt-4o-mini",
messages = [
    {"role": "user", "content": "You are a virtual assistant named Paper, skilled in general tasks like Alexa and Siri."},
    {"role": "user", "content": "what is coding??"}
]
)

print(completion.choices[0].message.content)
