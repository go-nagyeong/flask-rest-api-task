from api.database import db
from api.models.block import Block
from api.services.user_service import get_user_by_id
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from api.errors import UserAlreadyBlockedError, BlockedUserNotExistError, IncorrectBlockUserError

# 유저가 차단한 사용자 검색 (전체 게시물 조회할 때 필요)
def get_block_by_id(my_id):
    blocker = get_user_by_id(my_id)
    return Block.query.filter_by(blocker=blocker).all()

# 사용자 차단
def block_user(my_id, user_id):
    try:
        # 자기 자신 차단 못하게 예외 처리
        if my_id == user_id:
            raise IncorrectBlockUserError

        blocker = get_user_by_id(my_id)
        blocked = get_user_by_id(user_id)

        block = Block(blocker=blocker, blocked=blocked)

        db.session.add(block)
        db.session.commit()
        return block
        
    # 이미 차단한 사용자 차단 못하게 예외 처리
    except IntegrityError:
        db.session.rollback()
        raise UserAlreadyBlockedError
    
# 사용자 차단 취소
def unblock_user(my_id, user_id):
    try:
        # 자기 자신의 차단 취소에 대한 예외 처리
        if my_id == user_id:
            raise IncorrectBlockUserError

        blocker = get_user_by_id(my_id)
        blocked = get_user_by_id(user_id)
        
        block = Block.query.filter_by(blocker=blocker, blocked=blocked).first()

        db.session.delete(block)
        db.session.commit()

    # 차단하지 않은 사용자에 대한 차단 취소의 예외 처리
    except UnmappedInstanceError:
        db.session.rollback()
        raise BlockedUserNotExistError