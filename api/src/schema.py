from pydantic                   import BaseModel
        
class Inscription (BaseModel):
    idcourse                :   int
    idstudent               :   int
    class Config:
        orm_mode = True