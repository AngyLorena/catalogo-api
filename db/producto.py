from typing import  Dict
from pydantic import BaseModel

class ProductoInDB(BaseModel):
    codigo_prod: str
    nombre_prod : str
    unidad_de_medida_prod: str
    cantidad_prod: float
    costo_unit_prod:float
    precio_venta_prod:float
    proveedor: str
    almacen: str
 


database_producto = Dict[str, ProductoInDB]

database_producto ={
    "111111": ProductoInDB(**{"codigo_prod":"111111",
                            "nombre_prod":"Chocolate Corona",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":200,
                             "costo_unit_prod":2000,
                            "precio_venta_prod":3000,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "22222": ProductoInDB(**{"codigo_prod":"22222",
                            "nombre_prod":"Cebolla",
                            "unidad_de_medida_prod":"Libras",
                            "cantidad_prod":100,
                            "costo_unit_prod":800,
                            "precio_venta_prod":1400,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "33333": ProductoInDB(**{"codigo_prod":"33333",
                            "nombre_prod":"Agua",
                            "unidad_de_medida_prod":"Litros",
                            "cantidad_prod":300,
                            "costo_unit_prod":300,
                            "precio_venta_prod":900,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "44444": ProductoInDB(**{"codigo_prod":"44444",
                            "nombre_prod":"Cerveza",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":500,
                            "costo_unit_prod":2000,
                            "precio_venta_prod":2500,
                            "proveedor": "Bavaria",
                            "almacen": "AlmacenBogota"}),

    "55555": ProductoInDB(**{"codigo_prod":"55555",
                            "nombre_prod":"Panela",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":300,
                            "costo_unit_prod":900,
                            "precio_venta_prod":1300,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "66666": ProductoInDB(**{"codigo_prod":"66666",
                            "nombre_prod":"Chocoramo",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":100,
                            "costo_unit_prod":1100,
                            "precio_venta_prod":1600,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),
                
    "77777": ProductoInDB(**{"codigo_prod":"77777",
                            "nombre_prod":"Café",
                            "unidad_de_medida_prod":"Libras",
                            "cantidad_prod":150,
                            "costo_unit_prod":9000,
                            "precio_venta_prod":13000,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "88888": ProductoInDB(**{"codigo_prod":"88888",
                            "nombre_prod":"Coca Cola",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":350,
                            "costo_unit_prod":1500,
                            "precio_venta_prod":2000,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),

    "99999": ProductoInDB(**{"codigo_prod":"99999",
                            "nombre_prod":"Huevos AAA",
                            "unidad_de_medida_prod":"Unidades",
                            "cantidad_prod":350,
                            "costo_unit_prod":300,
                            "precio_venta_prod":400,
                            "proveedor": "Empresa ABC SAS",
                            "almacen": "AlmacenBogota"}),


}

def get_producto(codigo_prod: str):
    if codigo_prod in database_producto.keys():
        return database_producto[codigo_prod]
    else:
        return None

def update_producto(producto_in_db: ProductoInDB):
    database_producto[producto_in_db.codigo_prod] = producto_in_db
    return producto_in_db
                                    
