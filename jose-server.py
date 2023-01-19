#!/usr/bin/python3

import time
from sys import argv

from authlib.jose import jwt
from authlib.jose.errors import ExpiredTokenError

# token will expire in a week
TOKEN_TIMEOUT = 7 * 24 * 3600
# replace with YOUR OWN private key !!!

# replace with YOUR OWN public key !!!
PUBLIC_KEY = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApjlvc9QrmaNWye9a95qZ
h0FiI7zz2d89QIw145XcU0/eJFIt29Zvza57LIydsFLMvWWPmHrje1631QC3YJA5
xl3UMBIOJQJHwvMIdQHEl2LToo6d2sTfh+jNkgnsb9pQyVigje3L3mKHVTLacJYk
UkCvBqK9n9HryIMMNj8/KWRNCbrIsWOonicR0JzrdDafwbD2/H1qmsrzz/gOZFT+
IjjItf6KFHdYuuWlgElwrM7AFhHzvzQp8nw1L1ZVSpa5CGjMVCPJ+ri/HuF0U/JX
WHkKY1+uZ1SyHoJ1XdnaxnZYNE+BfWrnBRdRNCDkj6kpy/ofcf/fHWHROGmjt2P3
SQIDAQAB
-----END PUBLIC KEY-----
'''



# extract user_id from the token
def parse_token(token):
    claims = jwt.decode(token, PUBLIC_KEY)
    claims.validate()  # this line may raise ExpiredTokenError
    return claims


try:
    user_id = parse_token(argv[1])
    print(user_id)
# handle possible exception raised by claims.validate() in parse_token function
except ExpiredTokenError:
    print('token expired')
