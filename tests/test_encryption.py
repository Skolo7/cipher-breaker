import unittest

# Own
from encryption import ROT13Encryption, ROT47Encryption


class ROT13Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.rot13 = ROT13Encryption()

    def test_word_test_is_equal_to_GRFG(self):
        expected: str = "GRFG"
        actual: str = self.rot13.rot_13_encryption_mech(word_to_encrypt="TEST", tests=True)
        self.assertEqual(expected, actual, msg="Should be GRFG")

    def test_word_filip_is_equal_to_SVYVC(self):
        self.assertEqual(
            "SVYVC",
            self.rot13.rot_13_encryption_mech(word_to_encrypt="FILIP", tests=True),
            msg="Should be SVYVC",
        )


class ROT47Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.rot47 = ROT47Encryption()

    def test_word_test_is_equal_to_E6DE(self):
        pass


if __name__ == "__main__":
    unittest.main()
