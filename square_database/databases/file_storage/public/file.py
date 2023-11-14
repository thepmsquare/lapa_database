from sqlalchemy import Column, Integer, String, DateTime, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class File(Base):
    __tablename__ = 'file'

    file_id = Column(Integer, Sequence('file_id_seq'), primary_key=True, index=True)
    file_name_with_extension = Column(String, nullable=False, unique=True)
    file_extension = Column(String, nullable=False)
    file_date_created = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    file_last_modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    file_system_file_name_with_extension = Column(String, nullable=False)
    file_system_relative_path = Column(String, nullable=False)
    file_storage_token = Column(String, nullable=False, unique=True, index=True)
