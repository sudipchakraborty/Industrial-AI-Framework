from app.rag.rag_pipeline import (
    answer_question
)


class HRAgent:

    def execute(
        self,
        query
    ):

        return answer_question(
            query
        )