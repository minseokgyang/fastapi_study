#
# from datetime import datetime,timedelta
#
# from jaraco.functools import result_invoke
#
# #아래 코드는 제품 코드라고 함
# # def add(a:int, b:int) -> int:
# #     return a+b
# #
# # #아래 코드는 테스트 코드라고함
# # def test_add() -> None:
# #     #Given: 재료를 준비함. 무엇인가 주어졌을때
# #     a,b = 1, 1
# #
# #     #When: 테스트 대상이 되는 함수를 호출함.
# #     result = add(a,b) #result의 타입은 int
# #
# #     #Then:
# #     assert result == 2
# #     # if not result == 2: raise AssertionError
#
#
# #숫자2는 "배송일이야" 라고 배경을 모르는사람들에게 알릴수있음
# #magicnumber를 쓰지말자
# DELIVERY_DAY = 2
#
# def _is_holiday(day: datetime)->bool:
#     return day.weekday() > 5
#
#
#
# def get_eta(purchase_date:datetime) -> datetime:
#     current_date = purchase_date
#     remaining_days = DELIVERY_DAY
#
#     while remaining_days > 0:
#         current_date += timedelta(days=1)
#         if not _is_holiday(current_date):
#             remaining_days -= 1
#
#     return current_date
#
# def test_get_eta_2025_09_30() -> None:
#     result = get_eta(datetime(2025,9,30))
#     assert result == datetime(2025,10,1)
#
# def test_get_eta_2025_12_31() -> None:
#     result = get_eta(datetime(2025,12,31))
#     assert result == datetime(2026,1,2)
#
# def test_get_eta_2026_02_28() ->None:
#     result = get_eta(datetime(2026,2,28))
#     assert result == datetime(2026,3,3)
#
# def test_get_eta_2025_02_28() ->None:
#     result = get_eta(datetime(2025,2,28))
#     assert result == datetime(2025,3,4)
#
#


def test_simple() -> None:
    print("abc")
    assert True
