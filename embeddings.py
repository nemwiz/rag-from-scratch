import json
import os
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_client = OpenAI()


def gather_chunk_files() -> list[str]:
    return [f'{directory}/{file}' for directory, subdirectory, files in os.walk('chunks')
            for file in files if '.json' in file]


chunk_files = gather_chunk_files()

for index, chunk_file in enumerate(chunk_files, start=1):
    chunk_data = json.load(open(chunk_file))

    with open(chunk_file, 'w') as c:
        response = openai_api_client.embeddings.create(input=chunk_data['chunk_text'], model=os.environ.get('EMBEDDING_MODEL'))

        chunk_data['embeddings'] = response.data[0].embedding
        json.dump(chunk_data, c, indent=4)

    time.sleep(0.1)
    print(f'Processed chunks -> {index}/{len(chunk_files)}')
