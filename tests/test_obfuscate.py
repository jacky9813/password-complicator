import unittest
import typing

import password_complicator

class TestCases(typing.TypedDict):
    hash: typing.Literal[
            "sha3-512", "sha3-384", "sha3-256", "sha3-224",
            "sha512-256", "sha512-224",
            "sha512", "sha384", "sha256", "sha224",
            "sha1",
            "shake_128", "shake_256",
            "md5",
            "blake2b", "blake2s",
            "none"
        ]
    encoding: typing.Literal["url-b64", "base64", "base32", "ascii85"]
    password: str
    expected_result: str
    length: typing.Optional[int]

class TestObfuscate(unittest.TestCase):
    def test_obfuscate(self):
        cases: typing.Tuple[TestCases] = (
            {"hash": "sha512", "encoding": "base64", "password": "sha512-base64", "length": 18, "expected_result": "ohvQiEljMvSrBb5X1x"},
            {"hash": "sha256", "encoding": "ascii85", "password": "sha256-ascii85", "length": 14, "expected_result": "LmRmG%tbn<If.l"},
            {"hash": "sha1", "encoding": "base32", "password": "sha1-base32", "expected_result": "HUKG6Z6FVY2E"}
        )

        for case in cases:
            with self.subTest(f'{case["hash"]}-{case["encoding"]}'):
                self.assertEqual(
                    case["expected_result"],
                    password_complicator.obfuscate(case["password"], case["hash"], case["encoding"], case.get("length", 12))
                )
