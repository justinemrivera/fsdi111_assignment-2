
from app.database import get_db


def user_formatter(results: tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result[0]
        result_dict["first_name"] = result[1]
        result_dict["last_name"] = result[2]
        result_dict["hobbies"] = result[3]
        result_dict["active"] = result[4]
        out.append(result_dict)
    return out





def scan():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall
    cursor.close()
    return output_formatter(results)


def select(user_id):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=?",
        (user_id, )
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def deactivate_user(user_id):
    cursor = get_db()
    cursor.execute(
        "UPDATE user SET active=0 WHERE id=?",
        (user_id, )
    )
    cursor.commit()
    cursor.close()


def insert(first_name, last_name, hobbies=None, active=1):
    value_tuple = (first_name, last_name, hobbies, active)
    query = """
            INSERT INTO user (
                first_name,
                last_name,
                hobbies,
                active
            ) VALUES (
                ?, ?, ?, ?
            )
    """

    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id
