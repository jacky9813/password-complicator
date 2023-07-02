#!/usr/bin/env python3

import base64
import hashlib
import io
import typing


class NoneHash():
    """
        An object that has the same interface as standard hash function in hashlib
        does but doing nothing.

        This is solely for some maniac that refused to obfuscate the easy to remember
        password with hashing, making the password reversible.
    """
    def __init__(self, data: typing.Union[io.BufferedReader, bytes] = b'') -> None:
        self._data = io.BytesIO()
        self.update(data)

    def update(self, data: typing.Union[io.BufferedReader, bytes]) -> None:
        if isinstance(data, bytes):
            self._data.write(data)
        else:
            self._data.write(data.read())
        
    def digest(self) -> bytes:
        self._data.seek()
        return self._data.read()


HASH_OPTIONS = {
    **{
        # Tactics from JavaScript so that the function will actually return a new function
        # instead of referencing the same function, causing the algorithm last in the list
        # is always being used.
        hash_function: (lambda hf: (lambda *args, **kwargs: hashlib.new(hf, *args, **kwargs)))(hash_function)
        for hash_function in [
            "sha3_512", "sha3_384", "sha3_256", "sha3_224",
            "sha512_256", "sha512_224",
            "sha512", "sha384", "sha256", "sha224",
            "sha1",
            "md5",
            "blake2b", "blake2s"
        ]
    },
    "none": NoneHash
}
DEFAULT_HASH_FUNCTION = "sha512"

ENCODING_OPTIONS = {
    "url-b64": base64.urlsafe_b64encode,
    "base64": base64.b64encode,
    "base32": base64.b32encode,
    "ascii85": base64.a85encode,
    "hex": lambda b: b.hex()
}
DEFAULT_ENCODING_OPTION = "base64"

DEFAULT_LENGTH = 12


def obfuscate(password: str, hash_method: str, encode_method: str, length: int) -> str:
    raw_password: bytes = password.encode()
    hash_instance = HASH_OPTIONS[hash_method](raw_password)
    encoded_hash: bytes = ENCODING_OPTIONS[encode_method](hash_instance.digest())
    return encoded_hash.decode()[:length]
