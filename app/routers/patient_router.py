from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from ..database import get_db
from app.crud import patient_crud
from ..schemas.patient_schema import PatientCreate, PatientUpdate, PatientOut

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/", response_model=list[PatientOut])
def list_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return patient_crud.get_all(db, skip, limit)

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = patient_crud.get_by_id(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/", response_model=PatientOut, status_code=201)
def create_patient(data: PatientCreate, db: Session = Depends(get_db)):
    return patient_crud.create(db, data)

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(patient_id: int, data: PatientUpdate, db: Session = Depends(get_db)):
    patient = patient_crud.update(db, patient_id, data)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = patient_crud.delete(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return

@router.get("/", response_model=list[PatientOut])
def get_patients(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    """Return a paginated list of patients"""
    patients = patient_crud.get_all(db, skip=skip, limit=limit)
    return patients

