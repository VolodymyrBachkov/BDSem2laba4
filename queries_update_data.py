from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text
from models import Student, Course, Instructor, Enrollment, Review
from datetime import datetime

def update_data(session):
    while True:
        print("\n== Оновлення даних у таблицях ==")
        print("4.1. Оновити студента")
        print("4.2. Оновити курс")
        print("4.3. Оновити інструктора")
        print("4.4. Оновити запис про зарахування")
        print("4.5. Оновити огляд")
        print("4.6. Повернутися до меню")
        
        choice = input("Оберіть таблицю для оновлення даних (1-6): ").strip()
        
        if choice == '1':  # Оновлення студента
            print("\n== Студенти ==")
            print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Дата реєстрації':<20} |")
            print("-" * 95)
            students = session.query(Student).all()
            for student in students:
                print(f"| {student.id:<5} | {student.first_name:<20} | {student.last_name:<20} | {student.email:<30} | {student.enrollment_date:%Y-%m-%d} |")
            
            try:
                student_id = int(input("Введіть ID студента для оновлення: ").strip())
                student = session.query(Student).filter(Student.id == student_id).one()
                student.first_name = input(f"Введіть нове ім'я (зараз: {student.first_name}): ").strip()
                student.last_name = input(f"Введіть нове прізвище (зараз: {student.last_name}): ").strip()
                student.email = input(f"Введіть новий email (зараз: {student.email}): ").strip()
                session.commit()
                print("Дані студента успішно оновлено!")
            except NoResultFound:
                print("Студент з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при оновленні студента: {e}")
        
        elif choice == '2':  # Оновлення курсу
            print("\n== Курси ==")
            print(f"| {'ID':<5} | {'Назва':<20} | {'Опис':<50} | {'Ціна':<10} |")
            print("-" * 85)
            courses = session.query(Course).all()
            for course in courses:
                print(f"| {course.id:<5} | {course.name:<20} | {course.description:<50} | {course.price:<10} |")
            
            try:
                course_id = int(input("Введіть ID курсу для оновлення: ").strip())
                course = session.query(Course).filter(Course.id == course_id).one()
                course.name = input(f"Введіть нову назву курсу (зараз: {course.name}): ").strip()
                course.description = input(f"Введіть новий опис курсу (зараз: {course.description}): ").strip()
                course.price = float(input(f"Введіть нову ціну курсу (зараз: {course.price}): ").strip())
                session.commit()
                print("Дані курсу успішно оновлено!")
            except NoResultFound:
                print("Курс з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при оновленні курсу: {e}")
        
        elif choice == '3':  # Оновлення інструктора
            print("\n== Інструктори ==")
            print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} |")
            print("-" * 75)
            instructors = session.query(Instructor).all()
            for instructor in instructors:
                print(f"| {instructor.id:<5} | {instructor.first_name:<20} | {instructor.last_name:<20} | {instructor.email:<30} |")
            
            try:
                instructor_id = int(input("Введіть ID інструктора для оновлення: ").strip())
                instructor = session.query(Instructor).filter(Instructor.id == instructor_id).one()
                instructor.first_name = input(f"Введіть нове ім'я (зараз: {instructor.first_name}): ").strip()
                instructor.last_name = input(f"Введіть нове прізвище (зараз: {instructor.last_name}): ").strip()
                instructor.email = input(f"Введіть новий email (зараз: {instructor.email}): ").strip()
                instructor.bio = input(f"Введіть нове біо (зараз: {instructor.bio}): ").strip()
                session.commit()
                print("Дані інструктора успішно оновлено!")
            except NoResultFound:
                print("Інструктор з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при оновленні інструктора: {e}")
        
        elif choice == '4':  # Оновлення зарахування
            print("\n== Зарахування ==")
            print(f"| {'ID':<5} | {'Студент ID':<10} | {'Курс ID':<10} | {'Дата зарахування':<20} |")
            print("-" * 60)
            enrollments = session.query(Enrollment).all()
            for enrollment in enrollments:
                print(f"| {enrollment.id:<5} | {enrollment.student_id:<10} | {enrollment.course_id:<10} | {enrollment.enrollment_date:%Y-%m-%d} |")

            try:
                enrollment_id = int(input("Введіть ID запису про зарахування для оновлення: ").strip())
                enrollment = session.query(Enrollment).filter(Enrollment.id == enrollment_id).one()
                
                print("Студенти: ", end='')
                students = session.query(Student).all()
                student_list = ''
                for student in students:
                    student_list += f"{student.id} {student.first_name} {student.last_name}, "
                student_list = student_list[:-2] + ";"
                print(student_list)
                enrollment.student_id = int(input(f"Введіть новий студент ID (зараз: {enrollment.student_id}): ").strip())

                courses = session.query(Course).all()
                print("Курси: ", end='')
                course_list = ''
                for course in courses:
                    course_list += f"{course.id} {course.name}, "
                course_list = course_list[:-2] + ";"
                print(course_list)

                enrollment.course_id = int(input(f"Введіть новий курс ID (зараз: {enrollment.course_id}): ").strip())
                session.commit()
                print("Запис про зарахування успішно оновлено!")
            except NoResultFound:
                print("Запис про зарахування з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при оновленні запису про зарахування: {e}")
        
        elif choice == '5':  # Оновлення огляду
            print("\n== Огляди ==")
            print(f"| {'ID':<5} | {'Студент ID':<10} | {'Курс ID':<10} | {'Оцінка':<5} | {'Коментар':<50} |")
            print("-" * 70)
            reviews = session.query(Review).all()
            for review in reviews:
                print(f"| {review.id:<5} | {review.student_id:<10} | {review.course_id:<10} | {review.rating:<5} | {review.comment:<50} |")
            
            try:
                review_id = int(input("Введіть ID огляду для оновлення: ").strip())
                review = session.query(Review).filter(Review.id == review_id).one()

                # Оновлення студента та курсу для огляду
                print("Студенти: ", end='')
                students = session.query(Student).all()
                student_list = ''
                for student in students:
                    student_list += f"{student.id} {student.first_name} {student.last_name}, "
                student_list = student_list[:-2] + ";"
                print(student_list)
                review.student_id = int(input(f"Введіть новий студент ID (зараз: {review.student_id}): ").strip())
                
                courses = session.query(Course).all()
                print("Курси: ", end='')
                course_list = ''
                for course in courses:
                    course_list += f"{course.id} {course.name}, "
                course_list = course_list[:-2] + ";"
                print(course_list)
                review.course_id = int(input(f"Введіть новий курс ID (зараз: {review.course_id}): ").strip())

                # Оновлення оцінки та коментаря
                review.rating = int(input(f"Введіть нову оцінку (зараз: {review.rating}): ").strip())
                review.comment = input(f"Введіть новий коментар (зараз: {review.comment}): ").strip()
                session.commit()
                print("Огляд успішно оновлено!")
            except NoResultFound:
                print("Огляд з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при оновленні огляду: {e}")
        
        elif choice in ['6', 'q', 'quit', 'stop', 's', '']:
            break
        
        else:
            print("Невірний вибір, спробуйте ще раз.")
