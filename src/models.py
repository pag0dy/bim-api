from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# TODO: Mejorar y completar

class Base(DeclarativeBase):
    pass


class NivelDeInformacion(Base):
    __tablename__ = "nivel_de_informacion"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(5))
    description: Mapped[Optional[str]] = mapped_column(String(255))

    def __rep__(self) -> str:
        return f"Nivel de Información (id={self.id!r}, code={self.code!r})"


class TipoDeInformacion(Base):
    __tablename__ = "tipo_de_informacion"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(5))
    description: Mapped[Optional[str]] = mapped_column(String(255))

    def __rep__(self) -> str:
        return f"Tipo de Información (id={self.id!r}, code={self.code!r})"
    

class EstadoAvanceInformacion(Base):
    __tablename__ = "estado_avance_informacion"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(5))
    description: Mapped[Optional[str]] = mapped_column(String(255))

    def __rep__(self) -> str:
        return f"Estado de Avance de la Información (id={self.id!r}, code={self.code!r})"