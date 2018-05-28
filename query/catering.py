#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .query import Query

class CateringQuery(Query):
    __tablename__ = 'catering'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    meals = relationship("MealQuery", back_populates="catering")
    mealdate = relationship("MealDateQuery", back_populates="catering")

    def __init__(self, catering_id):
        self.id = catering_id

    def doQuery(self):
        return self.query(CateringQuery).filter_by(id=self.id).all()

    def __str__(self):
        return "Catering<{0}, \"{1}\">".format(self.id, self.name)
