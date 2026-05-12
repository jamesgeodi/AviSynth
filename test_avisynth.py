# test_avisynth.py
"""
Tests for AviSynth module.
"""

import unittest
from avisynth import AviSynth

class TestAviSynth(unittest.TestCase):
    """Test cases for AviSynth class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AviSynth()
        self.assertIsInstance(instance, AviSynth)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AviSynth()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
