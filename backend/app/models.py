from sqlalchemy import Column, Float, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class KLineData(Base):
    __tablename__ = "kline_data"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    interval = Column(String, index=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

