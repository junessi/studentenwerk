#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .query import Query
from .catering import CateringQuery
from .mealdate import MealDateQuery


class MealQuery(Query):
    __tablename__ = 'meal'

    meal_id = Column(Integer)
    name = Column(String)
    price0 = Column(String)
    price1 = Column(String)
    catering_id = Column(Integer, ForeignKey("catering.id"))
    catering = relationship(CateringQuery, back_populates="meals")
    mealdate = relationship(MealDateQuery, back_populates="meals")
    date_id = Column(Integer, ForeignKey("date.date_id"))

    __table_args__ = (
        PrimaryKeyConstraint('catering_id', 'date_id', 'meal_id'),
    )

    def __init__(self, catering_id, date_id):
        self.catering_id = catering_id
        self.date_id = date_id

    def doQuery(self):
        return self.query(MealQuery).filter_by(catering_id=self.catering_id)\
                                    .filter_by(date_id=self.date_id).all()

    def __str__(self):
        return "Meal<{0}, {1}, {2}, \"{3}\", \"{4}\", \"{5}\">".format(self.catering.id,
                                                             self.mealdate.date_id,
                                                             self.meal_id,
                                                             self.catering.name,
                                                             self.mealdate.text,
                                                             self.name)
