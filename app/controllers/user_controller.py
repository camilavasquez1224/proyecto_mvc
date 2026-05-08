from app import db
from app.models.user import User

def get_all_users():
    return [u.to_dict() for u in User.query.all()]

def get_user(id):
    user = User.query.get(id)
    return user.to_dict() if user else None

def create_user(data):
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return user.to_dict()

def update_user(id, data):
    user = User.query.get(id)
    if not user:
        return None
    user.name  = data.get('name',  user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return user.to_dict()

def delete_user(id):
    user = User.query.get(id)
    if not user:
        return None
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Usuario eliminado'}