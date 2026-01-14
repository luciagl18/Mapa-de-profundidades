"""
Visualizer Module
Módulo para visualizar la profundidad del libro de órdenes
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Optional


class DepthVisualizer:
    """
    Clase para visualizar datos de profundidad del libro de órdenes.
    """
    
    def __init__(self, style: str = 'darkgrid'):
        """
        Inicializa el visualizador.
        
        Args:
            style: Estilo de seaborn para los gráficos
        """
        sns.set_style(style)
        self.fig = None
        self.ax = None
        
    def plot_depth_chart(self, data: pd.DataFrame, title: str = "Mapa de Profundidad") -> plt.Figure:
        """
        Crea un gráfico de profundidad del libro de órdenes.
        
        Args:
            data: DataFrame con los datos del libro de órdenes
            title: Título del gráfico
            
        Returns:
            Figura de matplotlib
        """
        fig, ax = plt.subplots(figsize=(12, 6))
        
        bids = data[data['side'] == 'bid'].sort_values('price', ascending=False)
        asks = data[data['side'] == 'ask'].sort_values('price', ascending=True)
        
        # Calcular volumen acumulado
        bids['cumulative_volume'] = bids['volume'].cumsum()
        asks['cumulative_volume'] = asks['volume'].cumsum()
        
        # Graficar
        ax.fill_between(bids['price'], 0, bids['cumulative_volume'], 
                        alpha=0.5, color='green', label='Bids (Compra)')
        ax.fill_between(asks['price'], 0, asks['cumulative_volume'], 
                        alpha=0.5, color='red', label='Asks (Venta)')
        
        ax.set_xlabel('Precio')
        ax.set_ylabel('Volumen Acumulado')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        self.fig = fig
        self.ax = ax
        
        return fig
    
    def plot_order_distribution(self, data: pd.DataFrame, bins: int = 50) -> plt.Figure:
        """
        Crea un histograma de la distribución de órdenes.
        
        Args:
            data: DataFrame con los datos del libro de órdenes
            bins: Número de bins para el histograma
            
        Returns:
            Figura de matplotlib
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        bids = data[data['side'] == 'bid']
        asks = data[data['side'] == 'ask']
        
        ax1.hist(bids['volume'], bins=bins, alpha=0.7, color='green', edgecolor='black')
        ax1.set_xlabel('Volumen')
        ax1.set_ylabel('Frecuencia')
        ax1.set_title('Distribución de Órdenes de Compra')
        ax1.grid(True, alpha=0.3)
        
        ax2.hist(asks['volume'], bins=bins, alpha=0.7, color='red', edgecolor='black')
        ax2.set_xlabel('Volumen')
        ax2.set_ylabel('Frecuencia')
        ax2.set_title('Distribución de Órdenes de Venta')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        return fig
    
    def plot_price_levels(self, data: pd.DataFrame, top_n: int = 20) -> plt.Figure:
        """
        Crea un gráfico de barras de los niveles de precio principales.
        
        Args:
            data: DataFrame con los datos del libro de órdenes
            top_n: Número de niveles principales a mostrar
            
        Returns:
            Figura de matplotlib
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        
        bids = data[data['side'] == 'bid'].sort_values('price', ascending=False).head(top_n)
        asks = data[data['side'] == 'ask'].sort_values('price', ascending=True).head(top_n)
        
        y_pos_bids = np.arange(len(bids))
        y_pos_asks = np.arange(len(asks)) + len(bids) + 1
        
        ax.barh(y_pos_bids, bids['volume'], color='green', alpha=0.7, label='Bids')
        ax.barh(y_pos_asks, asks['volume'], color='red', alpha=0.7, label='Asks')
        
        ax.set_yticks(list(y_pos_bids) + list(y_pos_asks))
        ax.set_yticklabels([f"${p:.2f}" for p in bids['price']] + 
                          [f"${p:.2f}" for p in asks['price']])
        
        ax.set_xlabel('Volumen')
        ax.set_ylabel('Nivel de Precio')
        ax.set_title(f'Top {top_n} Niveles de Precio por Lado')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='x')
        
        return fig
    
    def save_figure(self, filepath: str, dpi: int = 300):
        """
        Guarda la figura actual.
        
        Args:
            filepath: Ruta donde guardar la figura
            dpi: Resolución de la imagen
        """
        if self.fig is not None:
            self.fig.savefig(filepath, dpi=dpi, bbox_inches='tight')
        else:
            raise ValueError("No hay figura para guardar")
