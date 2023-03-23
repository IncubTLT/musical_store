import secrets
import string

random = string.ascii_letters + string.digits
SECRET_KEY = ''.join(secrets.choice(random) for i in range(50))
