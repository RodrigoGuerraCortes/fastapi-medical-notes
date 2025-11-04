from pydantic import BaseModel, EmailStr
from datetime import date

class PatientBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date | None = None
    email: EmailStr | None = None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None
    email: EmailStr | None = None

class PatientOut(PatientBase):
    id: int

    class Config:
        from_attributes = True
