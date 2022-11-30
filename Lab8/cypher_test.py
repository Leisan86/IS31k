import unittest

from cypher import Cypher


def color_string(string: str) -> str:
    return f"\33[32m{string}\033[0m"


class MyTestCase(unittest.TestCase):
    def test1(self):
        Cypher.encryption("PyThOn")
        result: str = Cypher.decryption()
        self.assertEqual(result, color_string("PYTHON"))

    def test2(self):
        Cypher.encryption("Hello")
        result: str = Cypher.decryption()
        self.assertEqual(result, color_string("HELLO"))

    def test3(self):
        Cypher.encryption("lscpu")
        result = Cypher.decryption()
        self.assertEqual(result, color_string("LSCPU"))


if __name__ == "__main__":
    unittest.main()