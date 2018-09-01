#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .canteen import CanteenQuery
from .query import Query

Base = declarative_base()
class MealDateQuery(Query):
    __tablename__ = 'date'

    date_id = Column(Integer)
    text = Column(String)
    canteen_id = Column(Integer, ForeignKey("canteen.id"))
    canteen = relationship(CanteenQuery, back_populates="mealdate")
    meals = relationship("MealQuery", back_populates="mealdate")

    __table_args__ = (
        PrimaryKeyConstraint('canteen_id', 'date_id'),
    )

    def __init__(self, canteen_id):
        self.canteen_id = canteen_id

    def doQuery(self):
        return self.query(MealDateQuery).filter_by(canteen_id=self.canteen_id).all()

    def __str__(self):
        return "MealDate<{0}, {1}, {2}>".format(self.date_id, self.canteen.name, self.text)
