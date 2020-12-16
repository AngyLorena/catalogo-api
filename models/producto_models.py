from pydantic import BaseModel

class ProductoIn(BaseModel):
    codigo_prod: str
    nombre_prod : str
    unidad_de_medida_prod: str
    cantidad_prod: float
    costo_unit_prod:float
    precio_venta_prod:float
    proveedor: str
    almacen: str

class ProductoOut(BaseModel):
    codigo_prod: str
    nombre_prod : str
    unidad_de_medida_prod: str
    cantidad_prod: float
    precio_venta_prod:float
    almacen: str