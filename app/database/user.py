from sqlalchemy import Table, Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255), index=True)
    hash = Column(String(255))
