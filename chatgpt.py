import os
import openai
from config import apikey
openai.api_key = "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"
question="write a sample python program"
response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
print(response)