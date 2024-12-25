from engine import initialize_engine

from queries import add_sample_data, display_data, strategic_queries
from queries_add_data import add_data
from queries_delete_data import delete_data
from queries_update_data import update_data

from alembic.config import Config
from alembic import command

def run_migrations_online():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

def apply_migration_by_version(version):
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, version)

def show_tables(session):
    print("\n== Таблиці ==")
    display_data(session)

def add_sample_information(session):
    print("\n== Додавання прикладів даних ==")
    add_sample_data(session)

def create_migration():
    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, message="Added new migration", autogenerate=True)
    print("Міграцію створено!")

def configure_logging():
    logging_state = input("Увімкнути логування? (y/n): ").strip().lower()
    if logging_state == 'y':
        logging_state = True
    else:
        logging_state = False
    return logging_state

def menu():
    session = initialize_engine(logging_state=True)  # Ініціалізація сеансу з логуванням

    while True:
        print("\n== Меню ==")
        print("1. Показати таблиці")
        print("2. Додати приклади інформації")
        print("3. Додати інформацію")
        print("4. Змінення інформації")
        print("5. Видалення інформації інформації")
        print("6. Створити міграцію")
        print("7. Застосувати міграцію")
        print("  7.1. Застосувати останню")
        print("  7.2. Застосувати (вказати версію)")
        print("8. Запити, з застосуванням різних стратегій завантаження")
        print("9. Налаштування логування")
        print("10. Вихід")
        
        choice = input("Оберіть опцію (1-10): ").strip()

        if choice == '1':
            show_tables(session)
        elif choice == '2':
            add_sample_information(session)
        elif choice == '3':
            add_data(session)
        elif choice == '4':
            update_data(session)
        elif choice == '5':
            delete_data(session)
        elif choice == '6':
            create_migration()
        elif choice == '7':
            sub_choice = input("Оберіть опцію:\n1. Застосувати останню\n2. Застосувати за версією\n").strip()
            if sub_choice == '1':
                run_migrations_online()
            elif sub_choice == '2':
                version = input("Введіть версію міграції: ").strip()
                apply_migration_by_version(version)
        elif choice == '8':
            strategic_queries(session)
        elif choice == '9':
            logging_state = configure_logging()
            session.close()
            session = initialize_engine(logging_state=logging_state)  # Ініціалізація сеансу з логуванням
        elif choice in ['10', 'q', 'quit', 'stop', 's']:
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

def main():
    menu()

if __name__ == "__main__":
    main()
