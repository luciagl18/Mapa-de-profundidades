"""
Unit tests for DataLoader module
"""

import unittest
import pandas as pd
import json
import tempfile
import os
from mapa_profundidades.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    """Test cases for DataLoader class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.loader = DataLoader()
        self.test_data = {
            'bids': [[100.0, 1.5], [99.5, 2.0]],
            'asks': [[101.0, 1.2], [101.5, 1.8]]
        }
    
    def test_init(self):
        """Test DataLoader initialization."""
        self.assertIsNone(self.loader.data)
    
    def test_parse_order_book(self):
        """Test parsing order book data."""
        df = self.loader.parse_order_book(self.test_data)
        
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 4)
        self.assertIn('price', df.columns)
        self.assertIn('volume', df.columns)
        self.assertIn('side', df.columns)
        
        bids = df[df['side'] == 'bid']
        asks = df[df['side'] == 'ask']
        self.assertEqual(len(bids), 2)
        self.assertEqual(len(asks), 2)
    
    def test_load_from_json(self):
        """Test loading data from JSON file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump([{'price': 100, 'volume': 1.5, 'side': 'bid'}], f)
            temp_file = f.name
        
        try:
            df = self.loader.load_from_json(temp_file)
            self.assertIsInstance(df, pd.DataFrame)
            self.assertEqual(len(df), 1)
        finally:
            os.unlink(temp_file)
    
    def test_get_data(self):
        """Test getting loaded data."""
        self.assertIsNone(self.loader.get_data())
        
        df = self.loader.parse_order_book(self.test_data)
        self.loader.data = df
        
        retrieved_data = self.loader.get_data()
        self.assertIsNotNone(retrieved_data)
        self.assertEqual(len(retrieved_data), 4)


if __name__ == '__main__':
    unittest.main()
