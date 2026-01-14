"""
Mapa de Profundidades - Order Book Depth Analysis
Análisis de las profundidades de compra

Este paquete proporciona herramientas para analizar la profundidad del libro de órdenes
en mercados financieros.
"""

__version__ = "0.1.0"
__author__ = "luciagl18"

from .depth_analyzer import DepthAnalyzer
from .data_loader import DataLoader
from .visualizer import DepthVisualizer

__all__ = ['DepthAnalyzer', 'DataLoader', 'DepthVisualizer']
