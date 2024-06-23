from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--m!cojgyo811rfn90_rr1ds+abor(2f*kp&4tenp_i7q(h73y+"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_AUTO_FIELD='django.db.models.AutoField'



try:
    from .local import *
except ImportError:
    pass
