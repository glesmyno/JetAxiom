# test_jetaxiom.py
"""
Tests for JetAxiom module.
"""

import unittest
from jetaxiom import JetAxiom

class TestJetAxiom(unittest.TestCase):
    """Test cases for JetAxiom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JetAxiom()
        self.assertIsInstance(instance, JetAxiom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JetAxiom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
