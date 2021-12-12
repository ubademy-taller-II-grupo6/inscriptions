import uvicorn
import os
import inscriptions_api
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.src.exception_handlers import add_user_exception_handlers
from db import SessionLocal
from schema import Inscription

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

add_user_exception_handlers(app)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/inscriptions/conditions/enrollment/{idcourse}')
def get_enrollment_conditions(idcourse: int, db=Depends(db)):
    return inscriptions_api.get_enrollment_conditions(db, idcourse)


@app.get('/inscriptions/conditions/unenrollment/{idcourse}')
def get_enrollment_conditions(idcourse: int, db=Depends(db)):
    return inscriptions_api.get_unenrollment_conditions(db, idcourse)


@app.post('/inscriptions')
def enroll_student(inscription: Inscription, db=Depends(db)):
    return inscriptions_api.enroll_student(db, inscription)


@app.get('/inscriptions/course/{idcourse}')
def get_enrollments_by_course(idcourse: int, db=Depends(db)):
    return inscriptions_api.get_enrolled_students(db, idcourse)


@app.get('/inscriptions/student/{idstudent}')
def get_enrollments_by_student(idstudent: int, db=Depends(db)):
    return inscriptions_api.get_enrollments_by_student(db, idstudent)


@app.delete('/inscriptions')
def unenroll_student(inscription: Inscription, db=Depends(db)):
    return inscriptions_api.unenroll_student(db, inscription)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
