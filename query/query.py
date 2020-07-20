#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from .db import DB

Base = declarative_base()
class Query(Base):
    __abstract__ = True
    db = DB()

    def query(self, cls):
        return Query.db.query(cls)

    def save(self):
        return Query.db.save(self)

    def update(self, cls, id, data):
        return Query.db.update(cls, id, data)
