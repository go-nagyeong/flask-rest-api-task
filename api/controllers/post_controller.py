from flask import request, session
from flask_restful import Resource
from api.services.post_service import get_all_post, get_post_by_user_id, add_post, update_post, delete_post

class PostApi(Resource):
    # 전체 게시글 조회
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'status': 'fail', 'message': '로그인 필요'}

        posts = get_all_post(user_id)

        if len(posts) == 0:
            message = '전체 게시물이 없습니다'
        else:
            message = '전체 게시물 조회'

        return {
            'status': 'success', 
            'data': [post.serialize() for post in posts],
            'message': message
        }

class MyPostApi(Resource):
    # 내 게시글 조회
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'status': 'fail', 'message': '로그인 필요'}

        posts = get_post_by_user_id(user_id)

        if len(posts) == 0:
            message = '내 게시물이 없습니다'
        else:
            message = '내 게시물 조회'

        return {
            'status': 'success', 
            'data': [post.serialize() for post in posts],
            'message': message
        }
    
    # 게시글 작성
    def post(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'status': 'fail', 'message': '로그인 필요'}

        args = request.args
        title, content = args['title'], args['content']

        post = add_post(user_id, title, content)

        return {
            'status': 'success', 
            'data': post.serialize(),
            'message': '게시물 작성'
        }

class UpdatePostApi(Resource):
    # 게시글 수정
    def put(self, post_id):
        args = request.args
        title, content = args['title'], args['content']

        post = update_post(post_id, title, content)

        return {
            'status': 'success', 
            'data': post.serialize(),
            'message': '게시물 수정'
        }

    # 게시글 삭제
    def delete(self, post_id):
        delete_post(post_id)
        return {
            'status': 'success', 
            'message': '게시물 삭제'
        }