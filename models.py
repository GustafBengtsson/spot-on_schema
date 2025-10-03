from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EntsoePrices(Base):
    __tablename__ = "entsoe_prices"

    timestamp = Column(DateTime, primary_key=True)
    country_code = Column(String, primary_key=True)
    price_type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    retrieved_at = Column(DateTime, nullable=False)
    data_type = Column(String, nullable=True)
    market_product = Column(String, nullable=True)
    process_type = Column(String, nullable=True)
    business_type = Column(String, nullable=True)
    source = Column(String, nullable=True)

class EntsoeLoadForecast(Base):
    __tablename__ = "entsoe_load_forecast"

    timestamp = Column(DateTime, primary_key=True)
    country_code = Column(String, primary_key=True)
    variable = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    psr_type = Column(String, nullable=True)
    method = Column(String, nullable=False)
    retrieved_at = Column(DateTime, nullable=False)
    data_type = Column(String, nullable=True)
    source = Column(String, nullable=True)

class EntsoeCrossborderFlows(Base):
    __tablename__ = "entsoe_crossborder_flows"

    timestamp = Column(DateTime, primary_key=True)
    country_code_from = Column(String, primary_key=True)
    country_code_to = Column(String, primary_key=True)
    value = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    retrieved_at = Column(DateTime, nullable=False)
    data_type = Column(String, nullable=True)
    source = Column(String, nullable=True)

class EntsoeUnavailability(Base):
    __tablename__ = "entsoe_unavailability"

    timestamp = Column(DateTime, primary_key=True)
    country_code = Column(String, primary_key=True)
    docstatus = Column(String, nullable=True)
    periodstartupdate = Column(DateTime, nullable=True)
    periodendupdate = Column(DateTime, nullable=True)
    value = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    retrieved_at = Column(DateTime, nullable=False)
    source = Column(String, nullable=True)

class EntsoeHydroStorage(Base):
    __tablename__ = "entsoe_hydro_storage"

    timestamp = Column(DateTime, primary_key=True)
    country_code = Column(String, primary_key=True)
    value = Column(Float, nullable=False)
    method = Column(String, nullable=False)
    retrieved_at = Column(DateTime, nullable=False)
    source = Column(String, nullable=True)
