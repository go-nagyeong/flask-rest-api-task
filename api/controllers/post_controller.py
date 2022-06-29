from flask import request, session
from flask_restful import Resource
from api.services.post_service import get_all_post, get_post_by_user_id, add_post, update_post, delete_post
from api.errors import InvalidTitleError, InvalidContentError, PostNotExistError

class PostApi(Resource):
    # 전체 게시글 조회
    def get(self):
        user_id = session.get('user_id')
        posts = get_all_post(user_id)

        return {
            'status': 'success', 
            'data': [post.serialize() for post in posts],
            'message': '전체 게시물 조회'
        }

class MyPostApi(Resource):
    # 내 게시글 조회
    def get(self):
        user_id = session.get('user_id')
        posts = get_post_by_user_id(user_id)

        return {
            'status': 'success', 
            'data': [post.serialize() for post in posts],
            'message': '내 게시물 조회'
        }
    
    # 게시글 작성
    def post(self):
        try:
            user_id = session.get('user_id')

            args = request.args
            title, content = args['title'], args['content']

            post = add_post(user_id, title, content)

            return {
                'status': 'success', 
                'data': post.serialize(),
                'message': '게시물 작성'
            }
        
        except InvalidTitleError as e:
            return {'status': 'fail', 'message': e.message}
        except InvalidContentError as e:
            return {'status': 'fail', 'message': e.message}

class UpdatePostApi(Resource):
    # 게시글 수정
    def put(self, post_id):
        try:
            args = request.args
            title, content = args['title'], args['content']

            post = update_post(post_id, title, content)

            return {
                'status': 'success', 
                'data': post.serialize(),
                'message': '게시물 수정'
            }
        
        except PostNotExistError as e:
            return {'status': 'fail', 'message': e.message}

    # 게시글 삭제
    def delete(self, post_id):
        try:
            delete_post(post_id)
            return {
                'status': 'success', 
                'message': '게시물 삭제'
            }
        
        except PostNotExistError as e:
            return {'status': 'fail', 'message': e.message}
        