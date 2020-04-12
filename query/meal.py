#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Binary, ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from .query import Query
import array


class Meal(Query):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key = True)
    liked_users = Column(Binary)

    def __init__(self, id):
        self.id = id
        self.liked_users = array.array('L', [])

    def dict(self):
        return { "id": self.id, "liked_users": array.array('L', self.liked_users).tolist() }

    def query_meal(self):
        return self.query(Meal).filter_by(id=self.id).all()

    def update_data(self):
        self.update(Meal, self.id, {"liked_users": self.liked_users})


class MealQuery:
    def get_meal(self, meal_id):
        return Meal(meal_id).query_meal()

