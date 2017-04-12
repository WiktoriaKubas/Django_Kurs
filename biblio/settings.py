"""
Django settings for biblio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #katalog projektu zapamietany jako BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ph05nlww5ipyc5@t_b03dq@gr%+4uz=vn0iczoiyk!5)u@z4bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#czy nasz projekt jest rozwijany (TRUE/FALSE)

TEMPLATE_DEBUG = True
#tylko dla szablonow

ALLOWED_HOSTS = []
#wpisujemy tu jakie adresy internetowe maja prawo dostepu do tej aplikacji
#Kursowa aplikacja Django bedzie hostowana przez serwer ktory bedzie sie dopiero laczyl z nasza aplikacja
#Dla potrzeby developmentu wystarczy 127.0.0.1

# Application definition

#Aplikacje zainstalowane/ podpiete do naszego serwisu
INSTALLED_APPS = (
    'django.contrib.admin',           # panel administracyjny do tworzenia i modyfikacji
    'django.contrib.auth',            # aplikacja zajmujaca sie autoryzacja uzytkownikow
    'django.contrib.contenttypes',    # umozliwia nam tworzenie relacji miedzy dowolnymi obiektami w bazie
    'django.contrib.sessions',        # obsluga sesji, czyli ciasteczek
    'django.contrib.messages',        # wyswietlanie uzytkownikowi jakiegos komunikatu/powiadomienia
    'django.contrib.staticfiles',     # zarzadzanie plikami statycznymi (layout, ikonki)
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'biblio.urls' # sciezka pythonowa do pliku opisujacego strukture URL

WSGI_APPLICATION = 'biblio.wsgi.application' # co ma byc uruchamiane gry uruchamiamy serwer


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# W dalszych czesciech bedziemy uzywac PostgreSQL (TAK KOCHAM TO!!)
# dobry do aplikacji geolokalizacyjnych
# na razie sqlite3 nam wystarczy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Jezyk, domyslnie jest en-us
LANGUAGE_CODE = 'pl'

# Strefa czasowa, domyslnie UTC
TIME_ZONE = 'Europe/Warsaw'

# Internationalization
USE_I18N = True
# Localization
USE_L10N = True
# Uze TimeZone
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
# Pod jakim adresem beda pliki statyczne
