import numpy
from openai.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam, \
    ChatCompletionMessageParam

DOCUMENTS_DELIMITER = '+++++'

SYSTEM_PROMPT = f'''You are a helpful assistant who works at a company called Gitlab. 
Your job is to answer questions based on the company documents.
Use the provided documents delimited by {DOCUMENTS_DELIMITER} to answer questions. If the answer cannot be found in the documents, write
"Sorry, I could not find an answer to your question. Please try a different one." 
'''


def augmentation(user_question: str,
                 relevant_chunks: list[dict]) -> list[ChatCompletionMessageParam]:
    system_message = ChatCompletionSystemMessageParam(content=SYSTEM_PROMPT, role='system')

    user_prompt = ''

    for chunk in relevant_chunks:
        user_prompt += f"Document title: {chunk['title']}\n"
        user_prompt += f"Document description: {chunk['description']}\n\n"
        user_prompt += f"{chunk['chunk_text']}\n"
        user_prompt += f"{DOCUMENTS_DELIMITER}\n"

    user_prompt += f"\n\n Question: {user_question}"

    user_message = ChatCompletionUserMessageParam(content=user_prompt, role='user')

    # print('***** Prompt to be sent off to LLM *****')
    # print(SYSTEM_PROMPT)
    # print(user_prompt)

    return [system_message, user_message]
