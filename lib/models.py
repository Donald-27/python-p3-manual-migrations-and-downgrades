#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///migrations_test.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer(), primary_key=True)
    full_name = Column(String(), index=True)  
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: {self.full_name}, Grade {self.grade}"