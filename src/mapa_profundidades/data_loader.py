"""
Data Loader Module
Módulo para cargar y procesar datos de profundidad del mercado
"""

import pandas as pd
import numpy as np
from typing import Optional, Dict, List
import json


class DataLoader:
    """
    Clase para cargar datos de profundidad del libro de órdenes.
    """
    
    def __init__(self):
        """Inicializa el cargador de datos."""
        self.data = None
        
    def load_from_csv(self, filepath: str) -> pd.DataFrame:
        """
        Carga datos desde un archivo CSV.
        
        Args:
            filepath: Ruta al archivo CSV
            
        Returns:
            DataFrame con los datos cargados
        """
        try:
            self.data = pd.read_csv(filepath)
            return self.data
        except Exception as e:
            raise ValueError(f"Error al cargar el archivo CSV: {e}")
    
    def load_from_json(self, filepath: str) -> pd.DataFrame:
        """
        Carga datos desde un archivo JSON.
        
        Args:
            filepath: Ruta al archivo JSON
            
        Returns:
            DataFrame con los datos cargados
        """
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            self.data = pd.DataFrame(data)
            return self.data
        except Exception as e:
            raise ValueError(f"Error al cargar el archivo JSON: {e}")
    
    def parse_order_book(self, order_book: Dict) -> pd.DataFrame:
        """
        Parsea un libro de órdenes al formato estándar.
        
        Args:
            order_book: Diccionario con el libro de órdenes
            
        Returns:
            DataFrame con las órdenes procesadas
        """
        bids = pd.DataFrame(order_book.get('bids', []), columns=['price', 'volume'])
        asks = pd.DataFrame(order_book.get('asks', []), columns=['price', 'volume'])
        
        bids['side'] = 'bid'
        asks['side'] = 'ask'
        
        df = pd.concat([bids, asks], ignore_index=True)
        df['price'] = pd.to_numeric(df['price'])
        df['volume'] = pd.to_numeric(df['volume'])
        
        return df
    
    def get_data(self) -> Optional[pd.DataFrame]:
        """
        Obtiene los datos cargados.
        
        Returns:
            DataFrame con los datos o None si no hay datos
        """
        return self.data
