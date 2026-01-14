"""
Depth Analyzer Module
Módulo para analizar la profundidad del libro de órdenes
"""

import pandas as pd
import numpy as np
from typing import Tuple, Optional, Dict


class DepthAnalyzer:
    """
    Clase para analizar la profundidad del libro de órdenes.
    """
    
    def __init__(self, data: Optional[pd.DataFrame] = None):
        """
        Inicializa el analizador de profundidad.
        
        Args:
            data: DataFrame con los datos del libro de órdenes
        """
        self.data = data
        
    def set_data(self, data: pd.DataFrame):
        """
        Establece los datos a analizar.
        
        Args:
            data: DataFrame con los datos del libro de órdenes
        """
        self.data = data
    
    def calculate_depth(self, price_levels: int = 10) -> Dict:
        """
        Calcula la profundidad del mercado a diferentes niveles de precio.
        
        Args:
            price_levels: Número de niveles de precio a analizar
            
        Returns:
            Diccionario con las métricas de profundidad
        """
        if self.data is None:
            raise ValueError("No hay datos cargados para analizar")
        
        bids = self.data[self.data['side'] == 'bid'].sort_values('price', ascending=False).head(price_levels)
        asks = self.data[self.data['side'] == 'ask'].sort_values('price', ascending=True).head(price_levels)
        
        bid_depth = bids['volume'].sum()
        ask_depth = asks['volume'].sum()
        total_depth = bid_depth + ask_depth
        
        return {
            'bid_depth': bid_depth,
            'ask_depth': ask_depth,
            'total_depth': total_depth,
            'bid_ask_ratio': bid_depth / ask_depth if ask_depth > 0 else 0,
            'depth_imbalance': (bid_depth - ask_depth) / total_depth if total_depth > 0 else 0
        }
    
    def get_best_bid_ask(self) -> Tuple[float, float]:
        """
        Obtiene el mejor precio de compra y venta.
        
        Returns:
            Tupla con (mejor_bid, mejor_ask)
        """
        if self.data is None:
            raise ValueError("No hay datos cargados para analizar")
        
        bids = self.data[self.data['side'] == 'bid']
        asks = self.data[self.data['side'] == 'ask']
        
        best_bid = bids['price'].max() if len(bids) > 0 else 0
        best_ask = asks['price'].min() if len(asks) > 0 else 0
        
        return best_bid, best_ask
    
    def calculate_spread(self) -> Dict:
        """
        Calcula el spread del mercado.
        
        Returns:
            Diccionario con métricas del spread
        """
        best_bid, best_ask = self.get_best_bid_ask()
        
        spread = best_ask - best_bid
        mid_price = (best_bid + best_ask) / 2
        spread_percentage = (spread / mid_price * 100) if mid_price > 0 else 0
        
        return {
            'best_bid': best_bid,
            'best_ask': best_ask,
            'spread': spread,
            'mid_price': mid_price,
            'spread_percentage': spread_percentage
        }
    
    def analyze_liquidity(self, price_distance: float = 0.01) -> Dict:
        """
        Analiza la liquidez dentro de una distancia de precio específica.
        
        Args:
            price_distance: Distancia de precio desde el mejor bid/ask (en porcentaje)
            
        Returns:
            Diccionario con métricas de liquidez
        """
        if self.data is None:
            raise ValueError("No hay datos cargados para analizar")
        
        best_bid, best_ask = self.get_best_bid_ask()
        
        bid_threshold = best_bid * (1 - price_distance)
        ask_threshold = best_ask * (1 + price_distance)
        
        bids = self.data[(self.data['side'] == 'bid') & (self.data['price'] >= bid_threshold)]
        asks = self.data[(self.data['side'] == 'ask') & (self.data['price'] <= ask_threshold)]
        
        return {
            'bid_liquidity': bids['volume'].sum(),
            'ask_liquidity': asks['volume'].sum(),
            'total_liquidity': bids['volume'].sum() + asks['volume'].sum(),
            'bid_orders': len(bids),
            'ask_orders': len(asks)
        }
