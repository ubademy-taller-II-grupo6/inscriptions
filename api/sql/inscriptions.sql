create table inscriptions(
    idCourse integer,
    idStudent integer,
    primary key(idCourse, idstudent),
    foreign key (idCourse) references courses(id),
    foreign key (idStudent) references users(id)
)