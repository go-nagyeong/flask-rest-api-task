from api.database import db
from api.models.user import User

def get_user_by_id(id):
    return User.query.filter_by(id=id).first()

# 유저 아이디로 회원이 있는지 검사
def check_user(id):
    user = get_user_by_id(id)
    if not user:
        return False
    return user