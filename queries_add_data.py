from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text
from models import Student, Course, Instructor, Enrollment, Review
from datetime import datetime

def add_data(session):
    while True:
        print("\n== Додавання даних до таблиць ==")
        print("3.1. Додати студента")
        print("3.2. Додати курс")
        print("3.3. Додати інструктора")
        print("3.4. Додати запис про зарахування")
        print("3.5. Додати огляд")
        print("3.6. Повернутися до меню")
        
        choice = input("Оберіть таблицю для додавання даних (1-6): ").strip()
        
        if choice == '1':  # Додавання студента
            first_name = input("Введіть ім'я студента: ").strip()
            last_name = input("Введіть прізвище студента: ").strip()
            email = input("Введіть email студента: ").strip()
            enrollment_date = datetime.utcnow()
            student = Student(first_name=first_name, last_name=last_name, email=email, enrollment_date=enrollment_date)
            session.add(student)
        
        elif choice == '2':  # Додавання курсу
            name = input("Введіть назву курсу: ").strip()
            description = input("Введіть опис курсу (необов'язково): ").strip()
            price = float(input("Введіть ціну курсу: ").strip())
            course = Course(name=name, description=description, price=price)
            session.add(course)
        
        elif choice == '3':  # Додавання інструктора
            first_name = input("Введіть ім'я інструктора: ").strip()
            last_name = input("Введіть прізвище інструктора: ").strip()
            email = input("Введіть email інструктора: ").strip()
            bio = input("Введіть біографію інструктора (необов'язково): ").strip()
            instructor = Instructor(first_name=first_name, last_name=last_name, email=email, bio=bio)
            session.add(instructor)
        
        # Додавання зарахування
        elif choice == '4':
            try:
                print("Студенти: ", end='')
                students = session.query(Student).all()
                student_list = ''
                for student in students:
                    student_list += f"{student.id} {student.first_name} {student.last_name}, "
                student_list = student_list[:-2] + ";"
                print(student_list)
                
                student_id = int(input("Введіть ID студента: ").strip())
                student = session.query(Student).filter_by(id=student_id).one()  # Перевірка існування студента
            except NoResultFound:
                print("Студент з таким ID не знайдений.")
                continue  # Повертаємось до початку циклу або завершити залежно від вашої логіки

            try:
                courses = session.query(Course).all()
                print("Курси: ", end='')
                course_list = ''
                for course in courses:
                    course_list += f"{course.id} {course.name}, "
                course_list = course_list[:-2] + ";"
                print(course_list)
                
                course_id = int(input("Введіть ID курсу: ").strip())
                course = session.query(Course).filter_by(id=course_id).one()  # Перевірка існування курсу
            except NoResultFound:
                print("Курс з таким ID не знайдений.")
                continue  # Повертаємось до початку циклу або завершити

            enrollment_date = datetime.utcnow()
            enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=enrollment_date)
            session.add(enrollment)

        # Додавання огляду
        elif choice == '5':
            try:
                print("Студенти: ", end='')
                students = session.query(Student).all()
                student_list = ''
                for student in students:
                    student_list += f"{student.id} {student.first_name} {student.last_name}, "
                student_list = student_list[:-2] + ";"
                print(student_list)
                
                student_id = int(input("Введіть ID студента: ").strip())
                student = session.query(Student).filter_by(id=student_id).one()  # Перевірка існування студента
            except NoResultFound:
                print("Студент з таким ID не знайдений.")
                continue  # Повертаємось до початку циклу або завершити

            try:
                courses = session.query(Course).all()
                print("Курси: ", end='')
                course_list = ''
                for course in courses:
                    course_list += f"{course.id} {course.name}, "
                course_list = course_list[:-2] + ";"
                print(course_list)
                
                course_id = int(input("Введіть ID курсу: ").strip())
                course = session.query(Course).filter_by(id=course_id).one()  # Перевірка існування курсу
            except NoResultFound:
                print("Курс з таким ID не знайдений.")
                continue  # Повертаємось до початку циклу або завершити

            try:
                rating = int(input("Введіть рейтинг (1-5): ").strip())
                if rating > 0 and rating <= 5:
                    comment = input("Введіть коментар до курсу (необов'язково): ").strip()
                    review_date = datetime.utcnow()
                    review = Review(student_id=student_id, course_id=course_id, rating=rating, comment=comment, review_date=review_date)
                    session.add(review)
                else:
                    print("Рейтинг не може бути більше 5!")
            except ValueError:
                print("Невірний формат рейтингу. Будь ласка, введіть ціле число.")        

        elif choice in ['6', 'q', 'quit', 'stop', 's', '']:
            break
        
        else:
            print("Невірний вибір, спробуйте ще раз.")
        
        session.commit()
        print("Дані збереженно!")

