from sqlalchemy import Column, Integer, String, Date, Text
from database import Base

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    objetivo = Column(String(255), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    texto_principal = Column(Text, nullable=False)
    def __repr__(self):
        return f'<Campaign {self.nombre}>'