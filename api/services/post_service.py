from api.database import db
from api.models.post import Post
from api.services.user_service import get_user_by_id
from api.services.block_service import get_block_by_id

def get_post_by_user_id(id):
    user = get_user_by_id(id)
    return Post.query.filter_by(author=user).all()

def get_post_by_post_id(id):
    return Post.query.filter_by(id=id).first()

# 전체 게시글 조회 (차단한 사용자 게시물 제외)
def get_all_post(user_id):
    blocks = get_block_by_id(user_id)
    blocked_users_id = [block.blocked_id for block in blocks]
    return Post.query.filter(~(Post.author_id.in_(blocked_users_id))).all()

# 게시글 작성
def add_post(user_id, title, content):
    try:
        user = get_user_by_id(user_id)
        post = Post(author=user, title=title, content=content)
        db.session.add(post)
        db.session.commit()
        return post
    except:
        db.session.rollback()
        raise

# 게시글 수정
def update_post(post_id, title, content):
    post = get_post_by_post_id(post_id)
    post.update(title, content)
    return post

# 게시글 삭제
def delete_post(post_id):
    try:
        post = get_post_by_post_id(post_id)
        db.session.delete(post)
        db.session.commit()
    except:
        db.session.rollback()
        raise