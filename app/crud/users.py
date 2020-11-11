from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import User as UserSchema


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserSchema):
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = UserModel(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh()
    return db_user
