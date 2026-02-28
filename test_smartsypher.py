# test_smartsypher.py
"""
Tests for SmartSypher module.
"""

import unittest
from smartsypher import SmartSypher

class TestSmartSypher(unittest.TestCase):
    """Test cases for SmartSypher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartSypher()
        self.assertIsInstance(instance, SmartSypher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartSypher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
