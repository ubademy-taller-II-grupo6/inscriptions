from    sqlalchemy.orm  import Session
import  schema, models

def get_inscription (db: Session, idcourse: int = None, idstudent: int = None):
    if idcourse:
        if idstudent:
            return db.query (models.Inscription).filter(
                                models.Inscription.idcourse == idcourse).filter(
                                models.Inscription.idstudent == idstudent).first()

def get_inscriptions (db: Session):
    return db.query (models.Inscription).all()    

def get_inscriptions_by_student (db: Session, idstudent: int = None):
    if idstudent:
        return db.query (models.Inscription).filter(models.Inscription.idstudent == idstudent).all()
        
def get_inscriptions_by_course(db: Session, idcourse: int = None):
    if idcourse:
        return db.query (models.Inscription).filter(models.Inscription.idcourse == idcourse).all()
        
def create_inscription(db: Session, inscription: schema.Inscription):
    inscription_model  = models.Inscription(**inscription.dict())
    db.add(inscription_model)
    db.commit()
    db.refresh(inscription_model)
    return inscription_model

def delete_inscription(db: Session, inscription: schema.Inscription):
    inscription_model      = models.Inscription(**inscription.dict())
    inscription_to_delete  = db.query( models.Inscription).filter(
                                    models.Inscription.idcourse  == inscription_model.idcourse).filter(
                                    models.Inscription.idstudent == inscription_model.idstudent).first() 
    db.delete(inscription_to_delete)
    db.commit()
    return inscription

def error_message(message):
    return {
        'error': message
    }