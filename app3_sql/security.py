from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, "bob", "kA#HhY5K0K0Jtw^3&ArE*cz"),
    User(1, "user", "G63cQsu3mHSaC&2UFKqxWtl"),
    User(1, "guest", "s^3hK$*GAYKN0N6XBvBrdsp")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)