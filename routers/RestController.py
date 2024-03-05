from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return [{"Home": "OK"}]

@router.get("/users/")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]

@router.get("/users/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/users/{username}")
async def read_user(username: str):
    return {"username": username}