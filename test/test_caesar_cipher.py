from src.caesar_cipher import caesar_encrypt, caesar_decrypt
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_basic(self):
        self.assertEqual(caesar_encrypt("HELLO", 3), "KHOOR")
        self.assertEqual(caesar_encrypt("hello", 3), "khoor")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_decrypt("KHOOR", 3), "HELLO")
        self.assertEqual(caesar_decrypt("khoor", 3), "hello")

    def test_wraparound(self):
        self.assertEqual(caesar_encrypt("xyz", 3), "abc")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesar_decrypt("Mjqqt, Btwqi!", 5), "Hello, World!")

    def test_negative_shift(self):
        self.assertEqual(caesar_encrypt("abc", -1), "zab")

if __name__ == '__main__':
    unittest.main()

