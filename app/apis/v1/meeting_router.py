from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
#원래는 어떤 데이터베이스 를 쓰는 지 URL에 적을 필요가 없음
#강의에서만 이렇게함
#실전에서는 데이터베이스이름을 url에 넣지 마셈

@edgedb_router.post(
    "",
    description="meeting을 생성함"
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

@mysql_router.post(
    "",
    description="meeting을 생성합니다.",
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")