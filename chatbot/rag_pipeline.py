from chatbot.retriever import Retriever
from chatbot.chat_model import ask_gemini


class RAGPipeline:

    def __init__(self):

        self.retriever = Retriever()

    def ask(self, question: str, history=None):

        # Retrieve relevant documents from Pinecone
        documents = self.retriever.search(
            question,
            top_k=5
        )

        # Build the context from retrieved documents
        context = "\n\n".join(
            doc["text"]
            for doc in documents
        )

        # Generate the answer using the context
        # and previous conversation history
        answer = ask_gemini(
            question=question,
            context=context,
            history=history
        )

        return {
            "answer": answer,
            "sources": documents
        }