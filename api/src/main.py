import  uvicorn
import  os
import  crud
from    fastapi                 import FastAPI, Depends, HTTPException
from    fastapi.middleware.cors import CORSMiddleware
from    db                      import SessionLocal
from    schema                  import Inscription     
                                
app = FastAPI()
app.add_middleware( CORSMiddleware, 
                    allow_origins=["*"], 
                    allow_credentials=True, 
                    allow_methods=["*"],
                    allow_headers=["*"],
                    )

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
@app.get('/inscriptions/student/{idstudent}')
def get_inscriptions_by_student(idstudent: int, db=Depends(db)):
    inscriptions_by_student = crud.get_inscriptions_by_student(db, idstudent)
    if inscriptions_by_student:
        return inscriptions_by_student
    else:
        raise HTTPException(404, detail= crud.error_message(f'No existen inscripciones a cursos para el estudiante con id: {idstudent}'))
     
@app.get('/inscriptions/course/{idcourse}')
def get_inscriptions_by_course (idcourse:int, db=Depends(db)):
    inscriptions_by_course = crud.get_inscriptions_by_course(db,idcourse)
    if inscriptions_by_course:
        return inscriptions_by_course
    else:
        raise HTTPException(404, crud.error_message(f'No existen inscripciones de estudiantes para el curso con id: {idcourse}'))    

@app.post('/inscriptions/')
def create_inscription (inscription: Inscription, db=Depends(db)):
    return crud.create_inscription(db,inscription)

@app.delete('/inscriptions/')
def delete_inscription(inscription: Inscription, db=Depends(db)):
    inscription_exists = crud.get_inscription(db, inscription.idcourse, inscription.idstudent)
    if inscription_exists:
        return crud.delete_inscription (db, inscription)    
    else:    
        raise HTTPException(404, detail= crud.error_message(f'La inscripcion al curso con id: {inscription.idcourse} y estudiante con id: {inscription.idstudent} no existe'))

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)        
