
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES1 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY1 = 'django-insecure-e#tebi5f^lzoh-jsf@jq38s-a#weu=%5rmxui$f7%#!yknz_oe'