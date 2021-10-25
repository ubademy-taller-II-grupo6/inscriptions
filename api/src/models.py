from db                  import Base
from sqlalchemy          import Column, Integer
    
class Inscription(Base):
    __tablename__   = 'inscriptions'
    idcourse        = Column(Integer, primary_key = True)
    idstudent       = Column(Integer, primary_key = True)