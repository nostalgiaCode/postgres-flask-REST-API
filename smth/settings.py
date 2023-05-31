from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

   
# строка подключения
postgresql_database = "postgresql://postgres:1234@localhost:5432/questions"
   
class Base(DeclarativeBase): pass
  
# создаем модель, объекты которой будут храниться в бд
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(String)

    def __repr__(self):
        return "<Question(question='{}', answer='{}', created_at={})>"\
                .format(self.question, self.answer, self.created_at)