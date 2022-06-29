from api.database import db
from api.models.block import Block
from api.services.user_service import get_user_by_id

# 유저가 차단한 사용자 검색 (blocker 기준)
def get_block_by_id(my_id):
    blocker = get_user_by_id(my_id)
    return Block.query.filter_by(blocker=blocker).all()

# 사용자 차단
def block_user(my_id, user_id):
    try:
        blocker = get_user_by_id(my_id)
        blocked = get_user_by_id(user_id)
        block = Block(blocker=blocker, blocked=blocked)
        db.session.add(block)
        db.session.commit()
        return block
    except:
        db.session.rollback()
        raise

# 사용자 차단 취소
def unblock_user(my_id, user_id):
    try:
        blocker = get_user_by_id(my_id)
        blocked = get_user_by_id(user_id)
        
        block = Block.query.filter_by(blocker=blocker, blocked=blocked).first()

        db.session.delete(block)
        db.session.commit()
    except:
        db.session.rollback()
        raise