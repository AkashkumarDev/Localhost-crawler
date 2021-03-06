from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Record(Base):

    __tablename__ = "records"
    id = Column(Integer, primary_key=True)
    url = Column(Text)
    text = Column(Text)

    def __init__(self, url, text):
        self.url = url
        self.text = text
