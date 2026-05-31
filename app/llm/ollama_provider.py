# app/llm/ollama_provider.py

from langchain_ollama import ChatOllama

class OllamaProvider:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3"
        )

    def invoke(
        self,
        prompt
    ):

        response = self.llm.invoke(prompt)

        return response.content