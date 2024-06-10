import bcrypt

def encrypt_password(password):
    # Genera un hash de la contraseña utilizando bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def check_password(password, hashed_password):
    # Verifica si la contraseña coincide con el hash almacenado
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
