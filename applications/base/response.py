from rest_framework.response import Response

# API Status Error code 정의: 4xxx 통일
# 일반, 전체적으로 일어날 수 있는 에러 코드 : 40xx =>




# 단순 실패, 성공
operation_failure = Response(status=400, data={"message": "OPERATION_FAILURE"})
operation_success = Response(status=200, data={"message": "OPERATION_SUCCESS"})

# DB 정상 삭제
operation_deleted = Response(status=200, data={"message": "DATA_DELETED_SUCCESS"})

# 예외 처리 billing
certification_failure = Response(data={'message': 'NOT_ADMINISTRATOR_FAILURE', "status_code": 4101})