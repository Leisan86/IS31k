import unittest

from cipher import Cipher


def color_string(string: str) -> str:
    return f"\33[32m{string}\033[0m"


class MyTestCase(unittest.TestCase):
    def test1(self):
        Cipher.encryption("PyThOn")
        result: str = Cipher.decryption()
        self.assertEqual(result, color_string("PYTHON"))

    def test2(self):
        Cipher.encryption("Hello")
        result: str = Cipher.decryption()
        self.assertEqual(result, color_string("HELLO"))

    def test3(self):
        Cipher.encryption("lscpu")
        result = Cipher.decryption()
        self.assertEqual(result, color_string("LSCPU"))


if __name__ == "__main__":
    unittest.main()

    # print(123)
    # with open(".cipher", "w") as file:
    #     file.write('\n')
    #     file.close()
    # Я захотел после теста почистить файл .cipher, но в методе main() использовалась функция quit() из-за чего этот участок кода не работал
