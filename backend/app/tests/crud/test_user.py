from sqlalchemy.orm import Session

from app import crud
from app.schemas.user import UserCreate, UserUpdate
# some helpers for random input purpose
from app.tests.utils.utils import random_email, random_ascii_string

'''
    Create a normal user
'''
def test_create_user(db: Session) -> None:
    name = random_ascii_string()
    user_in = UserCreate(name=name)
    user = crud.user.create(db, obj_in=user_in)
    assert user.name == name

'''
    create an admin and see if it is really an admin
'''
def test_admin_user(db: Session) -> None:
    name = random_ascii_string()
    user_in = UserCreate(name=name, is_admin=True)
    user = crud.user.create(db, obj_in=user_in)
    is_admin = crud.user.is_admin(user)
    assert is_admin is True

'''
    create an assistant and see if it is really an assistant
'''
def test_assistant_user(db: Session) -> None:
    name = random_ascii_string()
    user_in = UserCreate(name=name, is_assistant=True)
    user = crud.user.create(db, obj_in=user_in)
    is_assistant = crud.user.is_assistant(user)
    assert  is_assistant is True

'''
    Test authenticate via user token
'''
def test_authenticate_user(db: Session) -> None:
    # create a user
    name = random_ascii_string()
    user_in = UserCreate(name=name)
    user = crud.user.create(db, obj_in=user_in)
    # try authenticate using the token from generated user
    authenticated_user = crud.user.authenticate(db, token=user.token)
    assert authenticated_user
    assert user.id == authenticated_user.id

''' 
    A non-exist user token should return None
'''
def test_not_authenticate_user(db: Session) -> None:
    token = random_ascii_string()
    # this random token should not exist in the database
    user = crud.user.authenticate(db, token=token)
    assert user is None

'''
    retrieve user using id, an identifier used internal only
'''
def test_get_by_user_id(db: Session) -> None:
    name = random_ascii_string()
    user_in = UserCreate(name=name, is_admin=True)
    user = crud.user.create(db, obj_in=user_in)
    userById = crud.user.getByUserId(user.id)
    assert userById.id == user.id


''' 
    A deleted user should be removed permently, return none when query
'''
def test_remove_user(db: Session) -> None:
    name = random_ascii_string()
    user_in = UserCreate(name=name, is_assistant=True)
    user = crud.user.create(db, obj_in=user_in)
    userId = user.id
    crud.user.remove(user)
    # find the same user id again 
    thisUser = crud.user.findById(userId)
    assert thisUser is None