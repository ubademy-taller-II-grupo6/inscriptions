import sqlalchemy
from sqlalchemy.orm import Session
import schema, db_models
from api.src.exceptions import InvalidOperationException
from api.src.utils import create_message_response


def get_enrollment_conditions(db: Session, idcourse):
    conditions = db.query(db_models.Course.enrollment_conditions).filter(db_models.Course.id == idcourse).first()
    if not conditions:
        raise InvalidOperationException("No se encontró el curso")
    response = {"Condiciones": conditions[0]}
    return response


def get_unenrollment_conditions(db: Session, idcourse):
    conditions = db.query(db_models.Course.unenrollment_conditions).filter(db_models.Course.id == idcourse).first()
    if not conditions:
        raise InvalidOperationException("No se encontró el curso")
    response = {"Condiciones": conditions[0]}
    return response


def get_enrolled_students(db: Session, idcourse):
    inscriptions = db.query(db_models.Inscription, db_models.User).filter \
        (db_models.Inscription.idcourse == idcourse).filter(db_models.User.id == db_models.Inscription.idstudent).all()
    if not inscriptions:
        return create_message_response("El curso no posee inscriptos")
    response = {}
    for inscription in inscriptions:
        student_data = inscription[1]
        response[student_data.id] = student_data.name + " " + student_data.lastname
    return response


def get_enrollments_by_student(db: Session, idstudent):
    courses = db.query(db_models.Inscription.idcourse, db_models.Course.title).join(db_models.Course).filter \
        (db_models.Inscription.idstudent == idstudent).all()
    if not courses:
        return create_message_response("El alumno no se ha inscripto a ningún curso")
    response = {}
    for course in courses:
        course_id = course[0]
        course_title = course[1]
        response[course_id] = course_title
    return response


def enroll_student(db: Session, inscription: schema.Inscription):
    inscription_model = db_models.Inscription(**inscription.dict())
    db.add(inscription_model)
    try:
        db.commit()
    except sqlalchemy.exc.IntegrityError as e:
        if e.orig.pgcode == '23505':
            raise InvalidOperationException("El alumno ya se encuentra inscripto en el curso")
        db.rollback()
        raise InvalidOperationException(" Uno o mas campos son incorrectos")
    response = create_message_response("La inscripción se realizó con éxito")
    return response


def unenroll_student(db: Session, inscription: schema.Inscription):
    inscription_model = db_models.Inscription(**inscription.dict())
    result = db.query(db_models.Inscription).filter(
        db_models.Inscription.idcourse == inscription_model.idcourse).filter(
        db_models.Inscription.idstudent == inscription_model.idstudent).delete()
    if not result:
        raise InvalidOperationException("La operación no es válida")
    db.commit()
    return create_message_response("Desinscripción exitosa")
