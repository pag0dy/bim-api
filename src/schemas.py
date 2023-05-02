from pydantic import BaseModel
from typing import Optional

class BaseInformacion(BaseModel):
    name: str
    code: str
    description: Optional[str] = None


class NivelDeInformacion(BaseInformacion):
    pass

class TipoDeInformacion(BaseInformacion):
    pass

class EstadoAvanceInformacion(BaseInformacion):
    pass