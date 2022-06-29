from api.controllers.main_controller import MainApi
from api.controllers.auth_controller import AuthApi
from api.controllers.post_controller import PostApi, MyPostApi, UpdatePostApi
from api.controllers.block_controller import BlockApi

def init_routes(api):
    api.add_resource(MainApi, '/api/')
    api.add_resource(AuthApi, '/api/auth')
    api.add_resource(PostApi, '/api/post')
    api.add_resource(MyPostApi, '/api/post/my')
    api.add_resource(UpdatePostApi, '/api/post/my/<post_id>')
    api.add_resource(BlockApi, '/api/block/<user_id>')