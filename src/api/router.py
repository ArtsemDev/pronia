from fastapi import APIRouter
from fastapi.responses import UJSONResponse


router = APIRouter(
    prefix='/api',
    include_in_schema=False,
    default_response_class=UJSONResponse
)
