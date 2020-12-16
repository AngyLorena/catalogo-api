from pydantic import BaseModel
from datetime import datetime

class EntradaIn(BaseModel):

    codigo_prod: str
    cantidad_prod: int
    costo_prod_ent: float

class EntradaOut(BaseModel):
    numero_transaccion: int
    codigo_prod: str
    cantidad_prod: int
    date: datetime
    cantidad_actual: float
    costo_actual: float

class SalidaIn(BaseModel):

    codigo_prod: str
    cantidad_prod: int


class SalidaOut(BaseModel):
    numero_transaccion: int
    codigo_prod: str
    cantidad_prod: int
    date: datetime
    cantidad_actual: float