from models import Student, Course, Instructor, Enrollment, Review

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import lazyload
from sqlalchemy import func

import time

def lazy_loading_example(session):
    """
    Завантаження даних за стратегією Lazy Loading.
    """
    start_time = time.time()
    print("\n== Студенти з їх зарахуваннями (Lazy Loading) ==")
    students = session.query(Student).all()
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Зараховані курси':<50} |")
    print("-" * 80)
    for student in students:
        # При Lazy Loading пов'язані записи завантажуються лише при доступі до них
        enrolled_courses = ", ".join([enrollment.course.name for enrollment in student.enrollments])
        print(f"| {student.id:<5} | {student.first_name + ' ' + student.last_name:<20} | {enrolled_courses:<50} |")
    elapsed_time = time.time() - start_time
    print(f"\nЧас виконання Lazy Loading: {elapsed_time:.4f} секунд")

def eager_loading_example(session):
    """
    Завантаження даних за стратегією Eager Loading.
    """
    start_time = time.time()
    print("\n== Студенти з їх зарахуваннями (Eager Loading) ==")
    # Використання Eager Loading за допомогою `joinedload`
    students = session.query(Student).options(joinedload(Student.enrollments).joinedload(Enrollment.course)).all()
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Зараховані курси':<50} |")
    print("-" * 80)
    for student in students:
        enrolled_courses = ", ".join([enrollment.course.name for enrollment in student.enrollments])
        print(f"| {student.id:<5} | {student.first_name + ' ' + student.last_name:<20} | {enrolled_courses:<50} |")
    elapsed_time = time.time() - start_time
    print(f"\nЧас виконання Eager Loading: {elapsed_time:.4f} секунд")

def explicit_loading_example(session):
    """
    Завантаження даних за стратегією Explicit Loading.
    """
    start_time = time.time()
    print("\n== Студенти з їх зарахуваннями (Explicit Loading) ==")

    students = session.query(Student).options(lazyload(Student.enrollments)).all()
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Зараховані курси':<50} |")
    print("-" * 80)
    for student in students:
        # Завантаження пов'язаних даних вручну
        session.query(Enrollment).filter(Enrollment.student_id == student.id).all()
        enrolled_courses = ", ".join([enrollment.course.name for enrollment in student.enrollments])
        print(f"| {student.id:<5} | {student.first_name + ' ' + student.last_name:<20} | {enrolled_courses:<50} |")
    elapsed_time = time.time() - start_time
    print(f"\nЧас виконання Explicit Loading: {elapsed_time:.4f} секунд")

def aggregate_query_example(session):
    """
    Запит з використанням агрегатних функцій, сортування та фільтрації.
    """
    start_time = time.time()
    print("\n== Середня оцінка за курсами ==")
    print(f"| {'Курс':<20} | {'Середня оцінка':<15} | {'Кількість відгуків':<20} |")
    print("-" * 60)
    results = (
        session.query(
            Course.name,
            func.avg(Review.rating).label('average_rating'),
            func.count(Review.id).label('review_count')
        )
        .join(Review, Course.id == Review.course_id)
        .group_by(Course.name)
        .order_by(func.avg(Review.rating).desc())  # Сортування за середньою оцінкою
        .all()
    )
    for course_name, avg_rating, review_count in results:
        print(f"| {course_name:<20} | {avg_rating:<15.2f} | {review_count:<20} |")
    elapsed_time = time.time() - start_time
    print(f"\nЧас виконання запиту: {elapsed_time:.4f} секунд")
