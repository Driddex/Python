from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Настройка приложения Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Создаем объект SQLAlchemy
db = SQLAlchemy(app)

# Определяем модель данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный идентификатор
    name = db.Column(db.String(80), nullable=False)  # Имя пользователя

# Создаем таблицы, если они еще не существуют
with app.app_context():
    db.create_all()

# Добавление пользователя
@app.route('/add_user/<string:name>/<int:id>', methods=['POST'])
def add_user(name, id):
    new_user = User(id=id,name=name)  # Создаем нового пользователя
    db.session.add(new_user)     # Добавляем пользователя в сессию
    db.session.commit()           # Сохраняем изменения
    return f"Пользователь {name} успешно добавлен!", 201

# Получение всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # Извлекаем всех пользователей
    return {
        "users": [user.name for user in users]  # Возвращаем список имен пользователей
    }

if __name__ == "__main__":
    app.run(debug=True)