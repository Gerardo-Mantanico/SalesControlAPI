from sqlalchemy import Column, Integer, String, Double
from sqlalchemy.orm import declarative_base
from db.db import engine
Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key= True)
    codigo = Column(Integer)
    nombre = Column(String)
    Descripcion = Column(String)
    precio = Column (Double)

    Base.metadata.create_all(engine)

