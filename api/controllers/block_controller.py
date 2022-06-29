from flask import session
from flask_restful import Resource
from api.services.block_service import block_user, unblock_user
from api.errors import UserAlreadyBlockedError, BlockedUserNotExistError, IncorrectBlockUserError

class BlockApi(Resource):
    def put(self, user_id):
        try:
            my_id = session.get('user_id')
            block = block_user(my_id, user_id)

            return {
                'status': 'success',
                'data': block.serialize(),
                'message': '사용자 차단'
            }
            
        except IncorrectBlockUserError as e:
            return {'status': 'fail', 'message': e.message}
        except UserAlreadyBlockedError as e:
            return {'status': 'fail', 'message': e.message}

    def delete(self, user_id):
        try:
            my_id = session.get('user_id')

            unblock_user(my_id, user_id)

            return {
                'status': 'success',
                'message': '사용자 차단 취소'
            }

        except IncorrectBlockUserError as e:
            return {'status': 'fail', 'message': e.message}
        except BlockedUserNotExistError as e:
            return {'status': 'fail', 'message': e.message}
            