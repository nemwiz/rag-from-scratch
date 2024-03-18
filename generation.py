import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

openai_api_client = OpenAI()


def generation(prompt_messages: list[ChatCompletionMessageParam]) -> str:
    response = openai_api_client.chat.completions.create(
        messages=prompt_messages,
        model=os.environ.get('CHAT_COMPLETION_MODEL'),
        temperature=0,
    )

    return response.choices[0].message.content
