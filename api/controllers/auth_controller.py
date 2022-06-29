from flask import request, session
from flask_restful import Resource
from api.services.user_service import check_user

class AuthApi(Resource):
    def post(self):
        # 유저 게시물 작성을 위해 간단하게 세션 로그인 구현
        args = request.args

        user = check_user(args['id'])
        if not user:
            return {'status': 'fail', 'message': '존재하지 않는 계정'}

        session.pop("user_id", None)
        session['user_id'] = args['id']

        return {
            'status': 'success',
            'data': user.serialize(),
            'message': '로그인 성공'
        }
            