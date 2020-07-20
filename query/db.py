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

    def save(self, obj):
        ret = False
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = []
        try:
            obj_session = session.object_session(obj)
            if obj_session is not None:
                obj_session.add(obj)
                obj_session.commit()
            else:
                session.add(obj)
                session.commit()
            ret = True
        except:
            session.rollback()
            raise
        session.close()

        return ret

    def update(self, cls, id, data):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = []
        try:
            result = session.query(cls).filter(cls.id == id).update(data)
            session.commit()
        except:
            session.rollback()
            raise
        session.close()

        return result

