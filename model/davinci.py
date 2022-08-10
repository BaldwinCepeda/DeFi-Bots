import os
import openai

openai.api_key = "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"

response=openai.Completion.create(
    model="text-davinci-002",
    prompt="what is. fruit",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
