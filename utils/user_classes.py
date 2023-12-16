from app.global_code.helpful_functions import connecttomysql, create_logger_error, log_it, log_exceptions
import os


class users:
    db = 'iris_v2'

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.date = data['date']
        self.name = data['name']

    @staticmethod
    @log_exceptions
    def save(data):

        query = 'INSERT INTO users (user_id, date, name) VALUES (%(user_id)s, %(date)s, %(name)s);'

        x = connecttomysql(users.db).query_db(query, data)
        return x

    @staticmethod
    @log_exceptions
    def select_all():
        query = 'SELECT * FROM users'

        x = connecttomysql(users.db).query_db(query)
        return x

if __name__ == '__main__':
    data = {'user_id': '1', 'date': '2021-04-01', 'name': 'Main'}
    users.save(data)
    print(users.select_all())
