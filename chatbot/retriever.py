from chatbot.vector_store import VectorStore
from chatbot.embeddings import embed_text


class Retriever:

    def __init__(self):

        self.index = VectorStore().get_index()

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = embed_text(query)

        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True
        )

        documents = []

        for match in results.matches:

            documents.append(
                {
                    "score": match.score,
                    "text": match.metadata["text"]
                }
            )

        return documents