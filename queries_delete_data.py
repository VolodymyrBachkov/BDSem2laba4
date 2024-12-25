from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text
from models import Student, Course, Instructor, Enrollment, Review
from datetime import datetime

def delete_data(session):
    while True:
        print("\n== Видалення даних з таблиць ==")
        print("5.1. Видалити студента")
        print("5.2. Видалити курс")
        print("5.3. Видалити інструктора")
        print("5.4. Видалити запис про зарахування")
        print("5.5. Видалити огляд")
        print("5.6. Повернутися до меню")
        
        choice = input("Оберіть таблицю для видалення даних (1-6): ").strip()
        
        if choice == '1':  # Видалення студента
            try:
                print("\n== Студенти ==")
                print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Дата реєстрації':<20} |")
                print("-" * 95)
                students = session.query(Student).all()
                for student in students:
                    print(f"| {student.id:<5} | {student.first_name:<20} | {student.last_name:<20} | {student.email:<30} | {student.enrollment_date:%Y-%m-%d} |")
               
                student_id = int(input("Введіть ID студента для видалення: ").strip())
                student = session.query(Student).filter(Student.id == student_id).one()
                session.delete(student)
                session.commit()
                print("Студента успішно видалено!")
            except NoResultFound:
                print("Студент з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при видаленні студента: {e}")
        
        elif choice == '2':  # Видалення курсу
            try:
                print("\n== Курси ==")
                print(f"| {'ID':<5} | {'Назва':<30} | {'Опис':<50} | {'Вартість':<10} |")
                print("-" * 100)
                courses = session.query(Course).all()
                for course in courses:
                    print(f"| {course.id:<5} | {course.name:<30} | {course.description:<50} | {course.price:<8.2f} |")

                course_id = int(input("Введіть ID курсу для видалення: ").strip())
                course = session.query(Course).filter(Course.id == course_id).one()
                session.delete(course)
                session.commit()
                print("Курс успішно видалено!")
            except NoResultFound:
                print("Курс з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при видаленні курсу: {e}")
        
        elif choice == '3':  # Видалення інструктора
            try:
                print("\n== Інструктори ==")
                print(f"| {'ID':<5} | {'Ім`я':<20} | {'Прізвище':<20} | {'Email':<30} | {'Біографія':<40} |")
                print("-" * 115)
                instructors = session.query(Instructor).all()
                for instructor in instructors:
                    print(f"| {instructor.id:<5} | {instructor.first_name:<20} | {instructor.last_name:<20} | {instructor.email:<30} | {instructor.bio:<40} |")
               
                instructor_id = int(input("Введіть ID інструктора для видалення: ").strip())
                instructor = session.query(Instructor).filter(Instructor.id == instructor_id).one()
                session.delete(instructor)
                session.commit()
                print("Інструктора успішно видалено!")
            except NoResultFound:
                print("Інструктор з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при видаленні інструктора: {e}")
        
        elif choice == '4':  # Видалення зарахування
            try:
                print("\n== Реєстрації ==")
                print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Дата реєстрації':<20} |")
                print("-" * 60)
                enrollments = session.query(Enrollment).all()
                for enrollment in enrollments:
                    print(f"| {enrollment.id:<5} | {enrollment.student_id:<15} | {enrollment.course_id:<10} | {enrollment.enrollment_date:%Y-%m-%d} |")

                enrollment_id = int(input("Введіть ID запису про зарахування для видалення: ").strip())
                enrollment = session.query(Enrollment).filter(Enrollment.id == enrollment_id).one()
                session.delete(enrollment)
                session.commit()
                print("Запис про зарахування успішно видалено!")
            except NoResultFound:
                print("Запис про зарахування з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при видаленні запису про зарахування: {e}")
        
        elif choice == '5':  # Видалення огляду
            try:
                print("\n== Відгуки ==")
                print(f"| {'ID':<5} | {'Студент ID':<15} | {'Курс ID':<10} | {'Рейтинг':<10} | {'Коментар':<30} | {'Дата відгуку':<20} |")
                print("-" * 105)
                reviews = session.query(Review).all()
                for review in reviews:
                    print(f"| {review.id:<5} | {review.student_id:<15} | {review.course_id:<10} | {review.rating:<10} | {review.comment:<30} | {review.review_date:%Y-%m-%d} |")

                review_id = int(input("Введіть ID огляду для видалення: ").strip())
                review = session.query(Review).filter(Review.id == review_id).one()
                session.delete(review)
                session.commit()
                print("Огляд успішно видалено!")
            except NoResultFound:
                print("Огляд з таким ID не знайдений!")
            except Exception as e:
                print(f"Помилка при видаленні огляду: {e}")
        
        elif choice in ['6', 'q', 'quit', 'stop', 's', '']:
            break
        
        else:
            print("Невірний вибір, спробуйте ще раз.")
