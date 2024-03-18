import json
import os

import numpy
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_client = OpenAI()

TOP_NUMBER_OF_CHUNKS_TO_RETRIEVE = 3


def load_chunks_with_embeddings() -> list[dict]:
    return [json.load(open(f'{directory}/{file}')) for directory, subdirectory, files in os.walk('chunks')
            for file in files if '.json' in file]


def perform_vector_similarity(user_question_embedding: list[float],
                              stored_chunk_embeddings: list[dict]) -> list[dict]:
    chunks_with_similarity_score = [
        (
            numpy.dot(numpy.array(chunk['embeddings']), numpy.array(user_question_embedding)),
            chunk
        )
        for chunk in stored_chunk_embeddings
    ]

    chunks_sorted_by_similarity = sorted(chunks_with_similarity_score, reverse=True, key=lambda score: score[0])

    return [chunk_with_similarity[1] for chunk_with_similarity in chunks_sorted_by_similarity]


def retrieval(user_question: str) -> list[dict]:
    response = openai_api_client.embeddings.create(input=user_question, model=os.environ.get('EMBEDDING_MODEL'))
    embedding_from_user_question = response.data[0].embedding

    stored_chunk_embeddings = load_chunks_with_embeddings()

    all_chunks_with_similarity_score = perform_vector_similarity(embedding_from_user_question,
                                                                 stored_chunk_embeddings)

    three_most_relevant_chunk = all_chunks_with_similarity_score[:TOP_NUMBER_OF_CHUNKS_TO_RETRIEVE]

    return three_most_relevant_chunk
