from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    uf: str
    sexo: str

app = FastAPI()

users = []


@app.get('/')
def show_users():
    if len(users) == 0:
        return 'No registered users'

    return users

@app.get('/{email}')
def show_user(email: str):
    for usuario in users:
        if usuario['email'] == email:
            return usuario
    
    return 'User not found'

@app.post('/')
def resgister_user(user: User):
    for usuario in users:
        if usuario['email'] == user.email:
            return 'User already registered!'
        
    users.append(dict(user))
    return 'User successfully registered!'

@app.put('/')
def update_user(user: User):
    for usuario in users:
        if usuario['email'] == user.email:
            usuario['name'] = user.name
            usuario['email'] = user.email
            usuario['uf'] = user.uf
            usuario['sexo'] = user.sexo

            return 'User successfully upgraded!' 
    
    return 'User not up to date!'


@app.delete('/{email}')
def delete_user(email: str):
    for usuario in users:
        if usuario['email'] == email:
            users.remove(usuario)

            return 'User successfully removed!'
    
    return 'No users found with that email!'
