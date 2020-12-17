from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
import hashlib

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

# it is the repository of command for all possible database manipulation
# convert general function calls to database manupulation

# not finished


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        # place holder
        return False

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def get_user(db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    def create_user(db: Session, user: schemas.UserCreate):
        hashed_password = hashlib.pbkdf2_hmac(
            'sha256',  # The hash digest algorithm for HMAC
            user.passwordencode('utf-8'),  # Convert the password to bytes
            "",  # Provide the salt
            100000,  # It is recommended to use at least 100,000 iterations of SHA-256
            dklen=128  # Get a 128 byte key
        )
        db_user = models.User(
            email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user = CRUDUser(User)
