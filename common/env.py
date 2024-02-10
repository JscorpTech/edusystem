import os

import environ

environ.Env.read_env(os.path.join('.env'))

#####################
# Env uchun default qiymatlarni shu yerda berish kerak
#####################
env = environ.Env(
    DEBUG=(bool, False),
    CACHE_TIME=(int, 180),
    OTP_EXPIRE_TIME=(int, 2),
    VITE_LIVE=(bool, False)
)
