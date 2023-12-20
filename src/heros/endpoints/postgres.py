from core.db.sessions import get_db


def postgres_test():
    try:
        db = get_db()
        print(db)
    except Exception as e:
        print("CONNECTION POSTGRES ERROR", e)


postgres_test()
