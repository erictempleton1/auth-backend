from fastapi import Depends, FastAPI, Header, HTTPException
from .database import connection
from app import routers, crud, schemas, models

models.user.connection.Base.metadata.create_all(bind=connection.engine)
app = FastAPI()


def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_token_header(x_token: str = Header(...)):
    if x_token != 'fake-token':
        raise HTTPException(status_code=400, detail='X-Token header invalid')

app.include_router(
    routers.users.router,
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}}
)
