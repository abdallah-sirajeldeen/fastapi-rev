from datetime import datetime
import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from db.db_setup import Base
from sqlalchemy_utils import URLType
from db.models.user import User

from db.models.mixins import TimestampMixin


class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3


class Course(TimestampMixin, Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    created_by = relationship(User)
    sections = relationship("Section", back_populates="course")
    student_courses = relationship("StudentCourse", back_populates="course")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="courses")
    content = relationship("Content", back_populates="course")


class Section(TimestampMixin, Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="sections")
    content_blocks = relationship("Content", back_populates="section")


class ContentBlock(TimestampMixin, Base):
    __tablename__ = "content_blocks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    type = Column(Enum(ContentType))
    url = Column(URLType, nullable=True)

    section_id = Column(Integer, ForeignKey("sections.id"))
    section = relationship("Section", back_populates="content_blocks")
    content = relationship("Content", back_populates="content_block")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content_block")


class StudentCourse(TimestampMixin, Base):
    __tablename__ = "student_courses"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="student_courses")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="student_courses")
