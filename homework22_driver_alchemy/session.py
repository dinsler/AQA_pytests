from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

__engine = create_engine('mysql+pymysql://hanna:12345@localhost/hillel_example')

session: Session = sessionmaker(__engine)()
