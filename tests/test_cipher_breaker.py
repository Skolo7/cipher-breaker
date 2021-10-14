import unittest

from run import CipherBreaker

class TestCipherBreakerMain(unittest.TestCase):
    def setUp(self) -> None:
        self.cipher_breaker = CipherBreaker()

    def test_modules_var_type(self):
        moduels_type = type(self.cipher_breaker.modules)
        self.assertTrue(issubclass(moduels_type, dict), msg="Should be dict.")

    def test_modules_content(self):
        modules_content_on_key_one = self.cipher_breaker.modules.get(1)
        self.assertEqual(modules_content_on_key_one, "Mthod to build")




if __name__ == '__main__':
    unittest.main()
