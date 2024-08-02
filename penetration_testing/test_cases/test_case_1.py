import unittest
from penetration_testing.test_manager import TestManager

class TestCase1(unittest.TestCase):
    def setUp(self):
        self.test_manager = TestManager()

    def test_network_test(self):
        target = "192.168.1.1"
        test_type = "network"
        test_results = self.test_manager.run_test(target, test_type)
        self.assertIsNotNone(test_results)
        self.assertIn("nmap", test_results)
        self.assertIn("nessus", test_results)

    def test_web_test(self):
        target = "example.com"
        test_type = "web"
        test_results = self.test_manager.run_test(target, test_type)
        self.assertIsNotNone(test_results)
        self.assertIn("burp", test_results)

    def test_os_test(self):
        target = "192.168.1.2"
        test_type = "os"
        test_results = self.test_manager.run_test(target, test_type)
        self.assertIsNotNone(test_results)
        self.assertIn("metasploit", test_results)

if __name__ == "__main__":
    unittest.main()
