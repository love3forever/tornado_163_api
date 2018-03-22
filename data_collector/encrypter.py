#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/3/19
# @Author  : wangmengcn (eclipse_sv@163.com)
# @Site    : https://eclipsesv.com

import os
from time import time
from functools import wraps
import base64
import codecs
from functools import lru_cache

from Crypto.Cipher import AES

modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'

def time_profile(func):
    @wraps(func)
    def inner_func(*args,**kwargs):
        print('encrypte started')
        start = time()
        result = func(*args,**kwargs)
        end = time()
        print('encrypting costs:{}'.format(end-start))
        return result
    return inner_func

def createSecretKey(size):
    return (''.join(map(lambda xx: hex(xx)[2:],
                        os.urandom(size))))[0:16]


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    if not isinstance(text, str):
        text = str(object=text, encoding='utf-8', errors='strict')
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    text = bytes(text, encoding="utf8")
    rs = int(codecs.encode(text, encoding='hex', errors='strict'), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


# @lru_cache()
@time_profile
def encrypted_request(text):
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': str(object=encText, encoding='utf-8', errors='strict'),
        'encSecKey': encSecKey
    }
    return data
