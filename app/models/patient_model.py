from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from ..database import Base

class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(80), nullable=False)
    last_name: Mapped[str] = mapped_column(String(80), nullable=False)
    birth_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    email: Mapped[str | None] = mapped_column(String(160), unique=True)