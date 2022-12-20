from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.repository.jobs import list_jobs, retreive_job
from db.sessions import get_db

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=True)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):  # new
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/home_page.html", {"request": request, "jobs": jobs, "msg": msg}  # new
    )


@router.get("/details/{id}")
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse(
        "jobs/detail.html", {"request": request, "job": job}
    )
