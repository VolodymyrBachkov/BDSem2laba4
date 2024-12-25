from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)

    enrollments = relationship('Enrollment', back_populates='student', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='student', cascade="all, delete-orphan")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)

    enrollments = relationship('Enrollment', back_populates='course', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='course', cascade="all, delete-orphan")

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    bio = Column(String(500), nullable=True)

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    enrollment_date = Column(DateTime, default=datetime.utcnow)

    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    review_date = Column(DateTime, default=datetime.utcnow)

    student = relationship('Student', back_populates='reviews')
    course = relationship('Course', back_populates='reviews')
