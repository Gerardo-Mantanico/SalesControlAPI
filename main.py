from fastapi import FastAPI, HTTPException
from db.db import session
from models.sucursales import Sucursal
from services import  sucursal_s

app = FastAPI()


@app.post("/sucusal")
async def create_sucursales(nombre: str, direccion: str):
    sucursal =  sucursal_s.create_sucursales(session, nombre, direccion)
    return {"sucursal registrada ": sucursal.nombre}


@app.get("/sucusal/{id}")
async def get_secursal(id: int):
    sucursal_query = session.query(Sucursal).filter(Sucursal.id_sucursal == id)
    if sucursal_query.first() is None:
        raise HTTPException(status_code=404, detail="Sucursal not found")
    return sucursal_query.first()




@app.get("/producto/{id}")
async def get_secursal(id: int):
    producto_query= session.query()
    sucursal_query = session.query(Sucursal).filter(Sucursal.id_sucursal == id)
    if sucursal_query.first() is None:
        raise HTTPException(status_code=404, detail="Sucursal not found")
    return sucursal_query.first()



@app.put("/sucursal/{id}")
async def update_sucursal(id: int, new_nombre: str, new_direccion: str):
    sucursal_query = session.query(Sucursal).filter(Sucursal.id_sucursal == id)
    sucursal = sucursal_query.first()
    if new_nombre:
        sucursal.nombre = new_nombre
    if new_direccion:
        sucursal.direccion = new_direccion
    session.add(sucursal)
    session.commit()


@app.delete("/sucursal/{id}")
async def delete_sucursal(id: int):
    sucursal = session.query(Sucursal).filter(Sucursal.id_sucursal == id).first()
    session.delete(sucursal)
    session.commit()
    return {"Sucursal deleted ": sucursal.nombre}
