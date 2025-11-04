from sqlalchemy.orm import Session
from ..models.patient_model import Patient
from ..schemas.patient_schema import PatientCreate, PatientUpdate

def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Patient).offset(skip).limit(limit).all()

def get_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def create(db: Session, patient: PatientCreate):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient




def update(db: Session, patient_id: int, data: PatientUpdate):
    db_patient = get_by_id(db, patient_id)
    if not db_patient:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_patient, key, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete(db: Session, patient_id: int):
    db_patient = get_by_id(db, patient_id)
    if not db_patient:
        return None
    db.delete(db_patient)
    db.commit()
    return db_patient
