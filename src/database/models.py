"""
ORM-модели для SQLite.
"""
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    proposals = relationship('Proposal', back_populates='user')

class Proposal(Base):
    __tablename__ = 'proposals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    client_name = Column(String(200))
    industry = Column(String(100))
    content = Column(Text)
    total_price = Column(Float)
    status = Column(String(50))
    generated_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship('User', back_populates='proposals')

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    industry = Column(String(100))
    employee_count = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    clients = relationship('Client', back_populates='company')

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('companies.id'))
    name = Column(String(200))
    contact_person = Column(String(200))
    email = Column(String(200))
    budget = Column(Float)
    
    company = relationship('Company', back_populates='clients')
