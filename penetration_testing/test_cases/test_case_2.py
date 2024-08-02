import unittest
from penetration_testing.test_manager import TestManager

class TestCase2(unittest.TestCase):
    def setUp(self):
        self.test_manager = TestManager()

    def test_invalid_target(self):
        target = "invalid_target"
        test_type = "network"
        with self.assertRaises(ValueError):
            self.test_manager.run_test(target, test_type)

    def test_invalid_test_type(self):
        target = "192.168.1.1"
        test_type = "invalid_test_type"
        with self.assertRaises(ValueError):
            self.test_manager.run_test(target, test_type)

    def test_network_test_with_nmap_failure(self):
        target = "192.168.1.1"
        test_type = "network"
        # Simulate Nmap failure
        with unittest.mock.patch("penetration_testing.test_manager.NetworkTestModule.run_nmap", side_effect=Exception("Nmap failed")):
            with self.assertRaises(Exception):
                self.test_manager.run_test(target, test_type)

if __name__ == "__main__":
    unittest.main()
