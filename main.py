from fastapi import FastAPI
from api import users, sections, courses
from db.db_setup import engine
from db.models import user , course


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My API",
    description="This is my API",
    version="1.0.0",
    terms_of_service="http://localhost:8000",
    contact={
        "name": "Abdullah Ahmed",
    }
)
app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
