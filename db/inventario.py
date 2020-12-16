from typing import  Dict
from pydantic import BaseModel
from datetime import datetime

class InventarioInDB(BaseModel):
    numero_transaccion: int=0
    codigo_prod: str
    cantidad_prod: float
    costo_prod_ent: float
    date: datetime = datetime.now()
    cantidad_actual: float
    costo_actual:float
    

database_entrada = []
generator = {"numero_transaccion":0}

def save_entrada(entrada_in_db: InventarioInDB):
    generator["numero_transaccion"] = generator["numero_transaccion"] + 1
    entrada_in_db.numero_transaccion = generator["numero_transaccion"]
    database_entrada.append(entrada_in_db)
    return entrada_in_db

database_salida = []
generator = {"numero_transaccion":0}

def save_salida(salida_in_db: InventarioInDB):
    generator["numero_transaccion"] = generator["numero_transaccion"] + 1
    salida_in_db.numero_transaccion = generator["numero_transaccion"]
    database_salida.append(salida_in_db)
    return salida_in_db