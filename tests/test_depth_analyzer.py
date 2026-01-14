"""
Unit tests for DepthAnalyzer module
"""

import unittest
import pandas as pd
from mapa_profundidades.depth_analyzer import DepthAnalyzer


class TestDepthAnalyzer(unittest.TestCase):
    """Test cases for DepthAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data = pd.DataFrame({
            'price': [100.0, 99.5, 99.0, 101.0, 101.5, 102.0],
            'volume': [1.5, 2.0, 1.8, 1.2, 1.8, 1.5],
            'side': ['bid', 'bid', 'bid', 'ask', 'ask', 'ask']
        })
        self.analyzer = DepthAnalyzer(self.test_data)
    
    def test_init(self):
        """Test DepthAnalyzer initialization."""
        analyzer = DepthAnalyzer()
        self.assertIsNone(analyzer.data)
        
        analyzer_with_data = DepthAnalyzer(self.test_data)
        self.assertIsNotNone(analyzer_with_data.data)
    
    def test_set_data(self):
        """Test setting data."""
        analyzer = DepthAnalyzer()
        analyzer.set_data(self.test_data)
        self.assertIsNotNone(analyzer.data)
        self.assertEqual(len(analyzer.data), 6)
    
    def test_get_best_bid_ask(self):
        """Test getting best bid and ask prices."""
        best_bid, best_ask = self.analyzer.get_best_bid_ask()
        
        self.assertEqual(best_bid, 100.0)
        self.assertEqual(best_ask, 101.0)
    
    def test_calculate_spread(self):
        """Test spread calculation."""
        spread_metrics = self.analyzer.calculate_spread()
        
        self.assertIn('best_bid', spread_metrics)
        self.assertIn('best_ask', spread_metrics)
        self.assertIn('spread', spread_metrics)
        self.assertIn('mid_price', spread_metrics)
        self.assertIn('spread_percentage', spread_metrics)
        
        self.assertEqual(spread_metrics['best_bid'], 100.0)
        self.assertEqual(spread_metrics['best_ask'], 101.0)
        self.assertEqual(spread_metrics['spread'], 1.0)
        self.assertEqual(spread_metrics['mid_price'], 100.5)
    
    def test_calculate_depth(self):
        """Test depth calculation."""
        depth_metrics = self.analyzer.calculate_depth(price_levels=10)
        
        self.assertIn('bid_depth', depth_metrics)
        self.assertIn('ask_depth', depth_metrics)
        self.assertIn('total_depth', depth_metrics)
        self.assertIn('bid_ask_ratio', depth_metrics)
        self.assertIn('depth_imbalance', depth_metrics)
        
        self.assertGreater(depth_metrics['bid_depth'], 0)
        self.assertGreater(depth_metrics['ask_depth'], 0)
        self.assertGreater(depth_metrics['total_depth'], 0)
    
    def test_analyze_liquidity(self):
        """Test liquidity analysis."""
        liquidity_metrics = self.analyzer.analyze_liquidity(price_distance=0.01)
        
        self.assertIn('bid_liquidity', liquidity_metrics)
        self.assertIn('ask_liquidity', liquidity_metrics)
        self.assertIn('total_liquidity', liquidity_metrics)
        self.assertIn('bid_orders', liquidity_metrics)
        self.assertIn('ask_orders', liquidity_metrics)
        
        self.assertGreaterEqual(liquidity_metrics['bid_orders'], 0)
        self.assertGreaterEqual(liquidity_metrics['ask_orders'], 0)


if __name__ == '__main__':
    unittest.main()
