import unittest
from unittest.mock import patch, mock_open
import hashlib
from encryption_module import CipherFactory, Encryption, CaesarCipher, SubstitutionCipher, TranspositionCipher

class TestEncryptionProgram(unittest.TestCase):

    def setUp(self):
        self.cipher_factory = CipherFactory.get_instance()
        self.encryption = Encryption()

    def test_caesar_cipher_encrypt(self):
        cipher = CaesarCipher(3)
        encrypted = cipher.encrypt("abcXYZ")
        self.assertEqual(encrypted, "defABC")

    def test_caesar_cipher_decrypt(self):
        cipher = CaesarCipher(3)
        decrypted = cipher.decrypt("defABC")
        self.assertEqual(decrypted, "abcXYZ")

    def test_substitution_cipher_encrypt(self):
        key = "phqgiumeaylnofdxjkrcvstzwb"
        cipher = SubstitutionCipher(key)
        encrypted = cipher.encrypt("abcXYZ")
        self.assertEqual(encrypted, "phqZWB")

    def test_substitution_cipher_decrypt(self):
        key = "phqgiumeaylnofdxjkrcvstzwb"
        cipher = SubstitutionCipher(key)
        decrypted = cipher.decrypt("phqZWB")
        self.assertEqual(decrypted, "abcXYZ")

    def test_transposition_cipher_encrypt(self):
        cipher = TranspositionCipher(8)
        encrypted = cipher.encrypt("WEAREDISCOVEREDRUN")
        self.assertEqual(encrypted, "WCUEONAVREERDEIDSR")

    def test_transposition_cipher_decrypt(self):
        cipher = TranspositionCipher(8)
        decrypted = cipher.decrypt("WCUEONAVREERDEIDSR")
        self.assertEqual(decrypted, "WEAREDISCOVEREDRUN")

    def test_sha256_encrypt(self):
        plaintext = "hello world"
        sha256_hash = self.encryption.sha256_encrypt(plaintext)
        self.assertEqual(sha256_hash, hashlib.sha256(plaintext.encode()).hexdigest())

    @patch("builtins.open", new_callable=mock_open, read_data="This is a test file.")
    def test_encrypt_file(self, mock_file):
        self.encryption.set_cipher(CaesarCipher(3))
        self.encryption.encrypt_file("input.txt", "output.txt")
        mock_file().write.assert_called_once_with("Wklv lv d whvw iloh.")

    @patch("builtins.open", new_callable=mock_open, read_data="Wklv lv d whvw iloh.")
    def test_decrypt_file(self, mock_file):
        self.encryption.set_cipher(CaesarCipher(3))
        self.encryption.decrypt_file("input.txt", "output.txt")
        mock_file().write.assert_called_once_with("This is a test file.")

    def test_set_cipher(self):
        cipher = CaesarCipher(3)
        self.encryption.set_cipher(cipher)
        self.assertEqual(self.encryption.cipher, cipher)

    def test_caesar_brute_force_decrypt(self):
        with patch("builtins.print") as mock_print:
            self.encryption.caesar_brute_force_decrypt("wklv lv d whvw")
            self.assertEqual(mock_print.call_count, 25)

if __name__ == "__main__":
    unittest.main()



