from fastapi import APIRouter

from app.api.schemas import (
    QueryRequest,
    QueryResponse
)

from app.routers.supervisor import (
    supervisor
)

router = APIRouter()

@router.post(
    "/chat",
    response_model=QueryResponse
)
def chat(
    request: QueryRequest
):

    result = supervisor(
        request.query
    )

    return QueryResponse(
        response=result
    )