from sqlalchemy import text
from models import Student, Course, Instructor, Enrollment, Review

from sqlalchemy.orm import joinedload
from sqlalchemy.orm import lazyload
from sqlalchemy import func

from strategic_queries import lazy_loading_example, eager_loading_example, explicit_loading_example, aggregate_query_example

def add_sample_data(session):
    # Додавання студентів
    students = [
        Student(first_name="John", last_name="Doe", email="john.doe@example.com"),
        Student(first_name="Jane", last_name="Smith", email="jane.smith@example.com"),
        Student(first_name="Michael", last_name="Johnson", email="michael.johnson@example.com"),
        Student(first_name="Emily", last_name="Davis", email="emily.davis@example.com"),
        Student(first_name="Chris", last_name="Brown", email="chris.brown@example.com"),
        Student(first_name="Sarah", last_name="Wilson", email="sarah.wilson@example.com"),
        Student(first_name="David", last_name="Anderson", email="david.anderson@example.com"),
        Student(first_name="Emma", last_name="Moore", email="emma.moore@example.com"),
        Student(first_name="James", last_name="Taylor", email="james.taylor@example.com"),
        Student(first_name="Sophia", last_name="Martin", email="sophia.martin@example.com"),
        Student(first_name="Daniel", last_name="Lee", email="daniel.lee@example.com"),
    ]

    # Додавання курсів
    courses = [
        Course(name="Python Programming", description="Learn Python from scratch", price=199.99),
        Course(name="Data Science", description="Introduction to Data Science", price=299.99),
        Course(name="Web Development", description="Master web technologies", price=249.99),
        Course(name="Machine Learning", description="Learn machine learning fundamentals", price=349.99),
    ]

    # Додавання інструкторів
    instructors = [
        Instructor(first_name="Alice", last_name="Brown", email="alice.brown@example.com", bio="Experienced Python instructor"),
        Instructor(first_name="Bob", last_name="Taylor", email="bob.taylor@example.com", bio="Expert in web development"),
        Instructor(first_name="Carol", last_name="Evans", email="carol.evans@example.com", bio="Data Science professional"),
        Instructor(first_name="Diana", last_name="White", email="diana.white@example.com", bio="Machine Learning specialist"),
    ]

    # Додавання реєстрацій
    enrollments = [
        Enrollment(student=students[0], course=courses[0]),
        Enrollment(student=students[1], course=courses[1]),
        Enrollment(student=students[2], course=courses[2]),
        Enrollment(student=students[3], course=courses[3]),
        Enrollment(student=students[4], course=courses[0]),
        Enrollment(student=students[5], course=courses[1]),
    ]

    # Додавання відгуків
    reviews = [
        Review(student=students[0], course=courses[0], rating=5, comment="Great course!"),
        Review(student=students[1], course=courses[1], rating=4, comment="Very informative."),
        Review(student=students[2], course=courses[2], rating=5, comment="Excellent instructor!"),
        Review(student=students[3], course=courses[3], rating=4, comment="Challenging, but worth it."),
    ]

    # Збереження в базу
    session.add_all(students + courses + instructors + enrollments + reviews)
    session.commit()

def display_data(session):
    # Вивід студентів
    print("\n== Студенти ==")
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Дата реєстрації':<20} |")
    print("-" * 95)
    students = session.query(Student).all()
    for student in students:
        print(f"| {student.id:<5} | {student.first_name:<20} | {student.last_name:<20} | {student.email:<30} | {student.enrollment_date:%Y-%m-%d} |")

    # Вивід курсів
    print("\n== Курси ==")
    print(f"| {'ID':<5} | {'Назва':<30} | {'Опис':<50} | {'Вартість':<10} |")
    print("-" * 100)
    courses = session.query(Course).all()
    for course in courses:
        print(f"| {course.id:<5} | {course.name:<30} | {course.description:<50} | {course.price:<8.2f} |")

    # Вивід інструкторів
    print("\n== Інструктори ==")
    print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Біографія':<40} |")
    print("-" * 115)
    instructors = session.query(Instructor).all()
    for instructor in instructors:
        print(f"| {instructor.id:<5} | {instructor.first_name:<20} | {instructor.last_name:<20} | {instructor.email:<30} | {instructor.bio:<40} |")

    # Вивід реєстрацій
    print("\n== Реєстрації ==")
    print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Дата реєстрації':<20} |")
    print("-" * 60)
    enrollments = session.query(Enrollment).all()
    for enrollment in enrollments:
        print(f"| {enrollment.id:<5} | {enrollment.student_id:<15} | {enrollment.course_id:<10} | {enrollment.enrollment_date:%Y-%m-%d} |")

    # Вивід відгуків
    print("\n== Відгуки ==")
    print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Рейтинг':<10} | {'Коментар':<30} | {'Дата відгуку':<20} |")
    print("-" * 105)
    reviews = session.query(Review).all()
    for review in reviews:
        print(f"| {review.id:<5} | {review.student_id:<15} | {review.course_id:<10} | {review.rating:<10} | {review.comment:<30} | {review.review_date:%Y-%m-%d} |")

def strategic_queries(session):
    while True:
        print("\n== Запити, з застосуванням різних стратегій завантаження ==")
        print("8.1. Завантаження даних за стратегією Lazy Loading")
        print("8.2. Завантаження даних за стратегією Eager Loading")
        print("8.3. Завантаження даних за стратегією Explicit Loading")
        print("8.4. Запит з використанням агрегатних функцій, сортування та фільтрації")
        print("8.5. Повернутися до меню")
        
        choice = input("Оберіть запит (1-5): ").strip()
        
        if choice == '1':
            lazy_loading_example(session)
        elif choice == '2':
            eager_loading_example(session)
        elif choice == '3':
            explicit_loading_example(session)
        elif choice == '4':
            aggregate_query_example(session)
        elif choice in ['5', 'q', 'quit', 'stop', 's', '']:
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")