import base64
import hashlib
import hmac

from flask import current_app


def __generate_password_digest(password: str) -> bytes:
    """
    Метод хэширует пароль
    """
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    """
    Метод кодирует хэшированный пароль
    """
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


def compare_passwords_hash(password_hash, other_password) -> bool:
    """
    Метод возвращает сравнение бинарных последовательностей чисел(из базы данных 'password_hash'
    и сгенерированный 'other_password'), возвращает либо True либо False
     """
    decoded_digest = base64.b64decode(password_hash)

    hash_digest = hashlib.pbkdf2_hmac(
        'sha256',
        other_password.encode('utf-8'),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"]
    )
    return hmac.compare_digest(decoded_digest, hash_digest)
