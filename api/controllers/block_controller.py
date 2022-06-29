from flask import session
from flask_restful import Resource
from api.services.block_service import block_user, unblock_user

class BlockApi(Resource):
    def put(self, id):
        my_id = session.get('user_id')
        if not my_id:
            return {'status': 'fail', 'message': '로그인 필요'}

        block = block_user(my_id, id)

        return {
            'status': 'success',
            'data': block.serialize(),
            'message': '사용자 차단'
        }

    def delete(self, id):
        my_id = session.get('user_id')
        if not my_id:
            return {'status': 'fail', 'message': '로그인 필요'}

        unblock_user(my_id, id)

        return {
            'status': 'success',
            'message': '사용자 차단 취소'
        }
            