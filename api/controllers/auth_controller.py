from flask import request, session
from flask_restful import Resource
from api.services.user_service import check_user
from api.errors import AccountNotExistError

class AuthApi(Resource):
    def post(self):
        try:
            # 유저 정보를 이용하는 기능(게시물 작성, 사용자 차단 등)을 위해 간단하게 세션 로그인 구현
            args = request.args

            user = check_user(args['id'])

            session.pop("user_id", None)
            session['user_id'] = args['id']

            return {
                'status': 'success',
                'data': user.serialize(),
                'message': '로그인 성공'
            }
            
        except AccountNotExistError as e:
            return {'status': 'fail', 'message': e.message}