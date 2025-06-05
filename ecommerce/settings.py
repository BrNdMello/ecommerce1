import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rwv&u18%6(4xgo+2c13(2vs^=jcc&0_!9%1hvv&)+2*mjk1z%w'

# DEBUG e ALLOWED_HOSTS
DEBUG = True  # Mantenha True para desenvolvimento. Coloque False em produção.
ALLOWED_HOSTS = []  # Com DEBUG=True, pode ficar vazio para localhost e 127.0.0.1

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # seus apps:
    'pedidos',
    'produtos',
    'carrinho',
    'categorias',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True, 
        'OPTIONS': { 
            'context_processors': [ 
                'django.template.context_processors.debug',
                'django.template.context_processors.request', 
                'django.contrib.auth.context_processors.auth', 
                'django.contrib.messages.context_processors.messages', 
                'carrinho.context_processors.carrinho_context', 
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [ 
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', 
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ===== CONFIGURAÇÕES DE MÍDIA =====
# Configuração para upload de imagens
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# ===== CONFIGURAÇÕES DO CARRINHO =====
# ID da sessão do carrinho
CARRINHO_SESSION_ID = 'carrinho'


# ===== CONFIGURAÇÕES DE LOGIN =====
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'produtos:lista'
LOGIN_REDIRECT_URL = 'produtos:lista'


# ===== CONFIGURAÇÕES DO MERCADO PAGO =====
MERCADOPAGO_PUBLIC_KEY = os.getenv('MERCADOPAGO_PUBLIC_KEY', 'TEST-74a10d13-059b-4fe7-a51c-549f30ab3db1')
MERCADOPAGO_ACCESS_TOKEN = os.getenv('MERCADOPAGO_ACCESS_TOKEN', 'APP_USR-6049984825376244-060218-3449bd486d3c68b9ed6b12b469c55d32-1188157375')


# ===== CONFIGURAÇÕES PIX =====
# Substitua pelos seus dados reais
MINHA_CHAVE_PIX = "sua-chave-pix@email.com"  # ou CPF, CNPJ, telefone, chave aleatória
NOME_BENEFICIARIO_PIX = "SEU NOME OU EMPRESA"  # Máximo 25 caracteres
CIDADE_BENEFICIARIO_PIX = "SAO PAULO"  # Máximo 15 caracteres, sem acentos


# ===== CONFIGURAÇÕES DE EMAIL =====
# Configure seu provedor de email para notificações de pedidos
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # ou seu provedor
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app'  # Use senha de aplicativo, não a senha normal
DEFAULT_FROM_EMAIL = 'seu-email@gmail.com'


# ===== CONFIGURAÇÕES DE SEGURANÇA PARA PRODUÇÃO =====
# Para produção, configure essas variáveis
if not DEBUG:
    ALLOWED_HOSTS = ['seudominio.com', 'www.seudominio.com']
    CSRF_TRUSTED_ORIGINS = ['https://seudominio.com', 'https://www.seudominio.com']