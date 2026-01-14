"""
Unit tests for DepthVisualizer module
"""

import unittest
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
from mapa_profundidades.visualizer import DepthVisualizer


class TestDepthVisualizer(unittest.TestCase):
    """Test cases for DepthVisualizer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data = pd.DataFrame({
            'price': [100.0, 99.5, 99.0, 101.0, 101.5, 102.0],
            'volume': [1.5, 2.0, 1.8, 1.2, 1.8, 1.5],
            'side': ['bid', 'bid', 'bid', 'ask', 'ask', 'ask']
        })
        self.visualizer = DepthVisualizer()
    
    def test_init(self):
        """Test DepthVisualizer initialization."""
        self.assertIsNone(self.visualizer.fig)
        self.assertIsNone(self.visualizer.ax)
    
    def test_plot_depth_chart(self):
        """Test depth chart creation."""
        fig = self.visualizer.plot_depth_chart(self.test_data)
        
        self.assertIsNotNone(fig)
        self.assertIsNotNone(self.visualizer.fig)
        self.assertIsNotNone(self.visualizer.ax)
    
    def test_plot_order_distribution(self):
        """Test order distribution plot creation."""
        fig = self.visualizer.plot_order_distribution(self.test_data)
        
        self.assertIsNotNone(fig)
    
    def test_plot_price_levels(self):
        """Test price levels plot creation."""
        fig = self.visualizer.plot_price_levels(self.test_data, top_n=3)
        
        self.assertIsNotNone(fig)


if __name__ == '__main__':
    unittest.main()
