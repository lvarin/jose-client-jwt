#!/usr/bin/python3

import time
from sys import argv

from authlib.jose import jwt
from authlib.jose.errors import ExpiredTokenError

# token will expire in a week
TOKEN_TIMEOUT = 7 * 24 * 3600
# replace with YOUR OWN private key !!!
PRIVATE_KEY = '''
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEApjlvc9QrmaNWye9a95qZh0FiI7zz2d89QIw145XcU0/eJFIt
29Zvza57LIydsFLMvWWPmHrje1631QC3YJA5xl3UMBIOJQJHwvMIdQHEl2LToo6d
2sTfh+jNkgnsb9pQyVigje3L3mKHVTLacJYkUkCvBqK9n9HryIMMNj8/KWRNCbrI
sWOonicR0JzrdDafwbD2/H1qmsrzz/gOZFT+IjjItf6KFHdYuuWlgElwrM7AFhHz
vzQp8nw1L1ZVSpa5CGjMVCPJ+ri/HuF0U/JXWHkKY1+uZ1SyHoJ1XdnaxnZYNE+B
fWrnBRdRNCDkj6kpy/ofcf/fHWHROGmjt2P3SQIDAQABAoIBAB7L2VhOYN2QI446
KFJjdDpY5MPWSB9/equwznMh2rYcv/1etFxceE5VG0D/tF9sl74nSNlpOygqPkja
Xx8m2W1lCOD3F2PH7l+yA0kaUL/zcV5WqexUOU3G1f9Ok12NxxXms6hX/ENxYb1p
NItTZdtPXJ4QHK21iMeXb/XE9gDG5XJrnDOxpe8aETns8J4Z4DItH8SDYxEL2OHM
UWdwBIXAxhWV17sNl8MCevzeH37DhiFkEI4777GT/8UpQ6unbY/9pIFI3UdoK6y/
VeKt8+ST6sK3SheUEtzsOWeyUf5ZCMPxbbnVRBG2xoPxJZpJ90CALPzDgoSx9CKR
kdSPCOECgYEAtmL65wuSqtu+0i/EAECFocqu8OlC9YJACRm+yq9P7TNlYKTMp27h
nsIVhGXm6dvqjCr/zxRcTFPzXfI1HdOtQ6Qk9Lq/9q3DRQYTRi2K4v2HqL+i9sFu
b7Tjysn9kGJEApzQTkXcdz2XjmIVbcVPOvsnS3gXWBS2XC2RQsTd830CgYEA6VB+
jPKQkR6gvw8njM8G1tUI+4p0RzVS62+m4Ach6ODiFZRhS9YXiycxPdU/pXQERgfz
nW3miqS9WnCt1A5QHHjm2hwUtPnxPMQG7LSY0h//GY/Kcm69mbiI5qBDez/pJmKy
55VxYpoxc2dTU82beJwgQjmSLuYqqNr9uxliRL0CgYEAjh4EeiKHb8F5KJj1tmiQ
eGjR9oEcnueWdEDubUs8EY3Z8fuYSONaxXVghOFOlG27jus2l6q63PMRkOPZxdsa
iLmP3m7ihBoULWW1gRqdvZBms/RXzMUfA8ZFNdA9V9NqQUrl+gfv6a5BuT3uirGT
slbf4Ku8LPM+wgbzyL5UYJUCgYEA2wgTVhTd/S7or5T1hy5P+F0UyriHQtZfmuE9
ozFu9yYveRzMXpqFjcBkbO0GjDgnTutmHBQxi1Tu4rnHpr0tHh2uc3JLSj8e5vIM
oilFEnaxUPj5kIY//tELzJ8F2u373mpoFBrq0Ct7YyDMTG9IlmjTq/hKMTcpM04r
R3ukEm0CgYBtI631qDKuYKJmvTKZTjaFxuJe4g46SKstBTktzn4Dikwu/3Z4gj7B
CRjqCqbXDnEuyfal69xiXKRe6oRFt2EACt75FuhCLLmpCcZQUy42lI7C5LzQCwn7
cz//erGKj/JusVValjfS9/fPTJukIlqvcGB/g3uZddDBzioSLBy8yQ==
-----END RSA PRIVATE KEY-----
'''


# store user_id in the generated token
def generate_token(user_id):
    header = {'alg': 'RS256'}
    payload = {
        'user_id': user_id,
        'exp': int(time.time() + TOKEN_TIMEOUT),
        'object': "objecto"
    }
    token = jwt.encode(header, payload, PRIVATE_KEY)
    token = token.decode()
    return token


# suppose the user_id is 12345
token = generate_token(argv[1])
print('JWT token:')
print(token)

