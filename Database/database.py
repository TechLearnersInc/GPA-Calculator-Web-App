from sqlalchemy import MetaData, create_engine, Table
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

class Database:
    def __int__(self):
        self.engine = create_engine('mysql+pymysql://inan:12345@'
                               'localhost/gpacalculator', pool_pre_ping=True)
        self.base = declarative_base(self.engine)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.metadata = MetaData()
        self.reflect_tables()

    def reflect_tables(self):
        GPA_HISTORY = Table('gpa_history', self.metadata, autoload=True, autoload_with=self.engine)
        GRADING_SYSTEM = Table('grading_system', self.metadata, autoload=True, autoload_with=self.engine)
        FEEDBACK = Table('feedback', self.metadata, autoload=True, autoload_with=self.engine)