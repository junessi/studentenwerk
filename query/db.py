#!/usr/bin/python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB:
    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://studentenwerk:studentenwerk_pwd@localhost/studentenwerk", pool_recycle=3600)

    def query(self, cls):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = []
        try:
            result = session.query(cls)
            session.commit()
        except:
            session.rollback()
            raise
        session.close()

        return result

