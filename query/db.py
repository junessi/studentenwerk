#!/usr/bin/python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB:
    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://studentenwerk:studentenwerk_pwd@localhost/studentenwerk")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def query(self, cls):
        result = []
        try:
            result = self.session.query(cls)
            self.session.commit()
        except:
            self.session.rollback()
            raise

        return result

