from app import dbBase, dbEngine
from sqlalchemy import Table


class GPA_HISTORY(dbBase):
    __table__ = Table(
        'gpa_history',
        dbBase.metadata,
        autoload=True,
        autoload_with=dbEngine
    )

class FEEDBACK(dbBase):
    __table__ = Table(
        'feedback',
        dbBase.metadata,
        autoload=True,
        autoload_with=dbEngine
    )