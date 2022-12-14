from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.users import UserCreate
from db.sessions import get_db
from db.repository.users import create_new_user
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/")
@router.post("/")
def create_user(request: 'Request', user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    context = {
        'user': user,
        'request': request,
    }
    return templates.TemplateResponse("general_pages/jobs_pages.html", context=context)
