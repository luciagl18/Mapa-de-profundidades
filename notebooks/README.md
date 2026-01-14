# Jupyter Notebook para Análisis Interactivo

Este directorio puede contener notebooks de Jupyter para análisis interactivos.

## Ejemplo de Uso

```python
import sys
sys.path.append('../src')

from mapa_profundidades import DataLoader, DepthAnalyzer, DepthVisualizer
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
loader = DataLoader()
data = loader.load_from_csv('../data/example_orderbook.csv')

# Analizar
analyzer = DepthAnalyzer(data)
metrics = analyzer.calculate_depth()

# Visualizar
visualizer = DepthVisualizer()
fig = visualizer.plot_depth_chart(data)
plt.show()
```
