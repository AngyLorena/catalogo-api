
from db.producto import ProductoInDB, get_producto,update_producto
from db.inventario import InventarioInDB,save_entrada, save_salida, database_entrada, database_salida 
from db.producto import database_producto
from models.producto_models import ProductoIn, ProductoOut
from models.inventario_models import SalidaIn, SalidaOut, EntradaIn, EntradaOut

import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

origins = [
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://localhost.tiangolo.com",
    "http://localhost", 
    "https://g3m4-g10-catalogo-app1.herokuapp.com/",
    "https://g3m4-g10-catalogo-app1.herokuapp.com/#/",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins =origins,
    allow_credentials =True,
    allow_methods =["*"],
    allow_headers=["*"],
)


@api.get("/producto/")
async def producto():
    return database_producto    


@api.put("/producto/entrada/")
async def ingreso_producto(entradaInventario_in: EntradaIn):

    producto_in_db = get_producto(entradaInventario_in.codigo_prod)

    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no ha sido creado")


    producto_in_db.costo_unit_prod = (((producto_in_db.cantidad_prod*producto_in_db.costo_unit_prod)+(entradaInventario_in.cantidad_prod*entradaInventario_in.costo_prod_ent))/(producto_in_db.cantidad_prod + entradaInventario_in.cantidad_prod))
    producto_in_db.cantidad_prod = producto_in_db.cantidad_prod + entradaInventario_in.cantidad_prod
    producto_in_db.precio_venta_prod= producto_in_db.costo_unit_prod*1.3

    update_producto(producto_in_db)


    entradaInventario_in_db = InventarioInDB(**entradaInventario_in.dict(), cantidad_actual= producto_in_db.cantidad_prod, costo_actual=producto_in_db.costo_unit_prod)
    entradaInventario_in_db = save_entrada(entradaInventario_in_db)

    entradaInventario_out = EntradaOut(**entradaInventario_in_db.dict())

    return  entradaInventario_out

@api.put("/producto/salida/")
async def salida_producto(salidaInventario_in: SalidaIn):

    producto_in_db = get_producto(salidaInventario_in.codigo_prod)

    if producto_in_db == None:
        raise HTTPException(status_code=404, detail="El producto no ha sido creado")

    if producto_in_db.cantidad_prod < salidaInventario_in.cantidad_prod:
        raise HTTPException(status_code=400, detail="No hay suficiente stock de inventario")


    producto_in_db.cantidad_prod = producto_in_db.cantidad_prod - salidaInventario_in.cantidad_prod
    update_producto(producto_in_db)
    

    salidaInventario_in_db = InventarioInDB(**salidaInventario_in.dict(), cantidad_actual= producto_in_db.cantidad_prod, costo_actual=producto_in_db.costo_unit_prod, costo_prod_ent=0)
    salidaInventario_in_db = save_salida(salidaInventario_in_db)

    salidaInventario_out = SalidaOut(**salidaInventario_in_db.dict())

    return  salidaInventario_out



