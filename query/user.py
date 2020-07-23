#!/usr/bin/python
#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .query import Query


class User(Query):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    openid = Column(String)
    last_commit_timestamp = Column(DateTime)

    def __init__(self, id = None, openid = ""):
        if id is not None:
            self.id = id

        if len(openid):
            self.openid = openid

    def query_info(self):
        return self.query(User).filter_by(id=self.id).all()

    def get_openid(self):
        return self.openid

    def dict(self):
        return {"id": self.id,
                "name": self.name,
                "openid": self.openid,
                "last_commit_timestamp": self.last_commit_timestamp}

    def __str__(self):
        return "User<{0}, \"{1}\", \"{2}\">".format(self.id, self.name, self.openid)

class UserQuery:
    def get_user_info(self, user_id):
        return User(id=user_id).query_info()

    def get_user_by_openid(self, openid):
        return User().query(User).filter_by(openid=openid).all()

