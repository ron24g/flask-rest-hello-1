from flask_sqlalchemy import SQLAlchemy
from main import app, db
from models import User

with app.app_context():
    users = [
            User(email="hasheduser@gmail.com", password="fakepassword1", is_active=True),
            User(email="anotherperson@snail.mail", password="fakepassword2", is_active=True)
        ]
    for user in users:
        db.session.add(user)
    db.session.commit()