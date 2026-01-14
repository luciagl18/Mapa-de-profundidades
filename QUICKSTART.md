# Guía de Inicio Rápido - Mapa de Profundidades

Esta guía te ayudará a comenzar con el análisis de profundidad del libro de órdenes en minutos.

## 1. Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/luciagl18/Mapa-de-profundidades.git
cd Mapa-de-profundidades

# Instalar dependencias
pip install -r requirements.txt

# O instalar el paquete completo
pip install -e .
```

## 2. Ejecutar el Primer Análisis

```bash
# Análisis básico con datos de ejemplo
python src/main.py data/example_orderbook.csv

# Con visualizaciones
python src/main.py data/example_orderbook.csv --visualize
```

## 3. Resultado Esperado

```
=== MÉTRICAS DE PROFUNDIDAD ===
Profundidad de Bids: 21.80
Profundidad de Asks: 21.00
Profundidad Total: 42.80
Ratio Bid/Ask: 1.04
Desequilibrio de Profundidad: 1.87%

=== MÉTRICAS DE SPREAD ===
Mejor Bid: $50000.00
Mejor Ask: $50001.00
Spread: $1.00
Precio Medio: $50000.50
Spread %: 0.20%

=== MÉTRICAS DE LIQUIDEZ ===
Liquidez de Bids: 21.80
Liquidez de Asks: 21.00
Liquidez Total: 42.80
Órdenes de Bid: 10
Órdenes de Ask: 10
```

## 4. Usar con Tus Propios Datos

### Formato CSV

Crea un archivo CSV con las siguientes columnas:

```csv
price,volume,side
50000.00,1.5,bid
50001.00,1.6,ask
```

### Formato JSON

O crea un archivo JSON con el siguiente formato:

```json
{
    "bids": [
        [50000.00, 1.5],
        [49999.50, 2.3]
    ],
    "asks": [
        [50001.00, 1.6],
        [50001.50, 2.1]
    ]
}
```

Luego ejecuta:

```bash
python src/main.py tu_archivo.csv --visualize --output resultados
```

## 5. Usar como Biblioteca Python

```python
from mapa_profundidades import DataLoader, DepthAnalyzer, DepthVisualizer

# Cargar datos
loader = DataLoader()
data = loader.load_from_csv('data/example_orderbook.csv')

# Analizar
analyzer = DepthAnalyzer(data)
metrics = analyzer.calculate_depth()
print(f"Profundidad Total: {metrics['total_depth']}")

# Visualizar
visualizer = DepthVisualizer()
fig = visualizer.plot_depth_chart(data)
visualizer.save_figure('mi_grafico.png')
```

## 6. Ejecutar Tests

```bash
# Todos los tests
python -m unittest discover tests/ -v

# Test específico
python -m unittest tests.test_depth_analyzer
```

## 7. Próximos Pasos

- Lee el [README.md](README.md) completo para más detalles
- Explora los ejemplos en la carpeta `data/`
- Revisa la [Guía de Contribución](CONTRIBUTING.md)
- Personaliza la configuración en `config/config.yaml`

## 8. Problemas Comunes

### Error: No module named 'mapa_profundidades'

Solución: Instala el paquete con `pip install -e .`

### Error: No se pueden generar visualizaciones

Solución: Asegúrate de tener matplotlib instalado: `pip install matplotlib`

### Los datos no se cargan correctamente

Solución: Verifica que tu archivo tiene el formato correcto (CSV o JSON) y las columnas necesarias.

## Ayuda

Si tienes preguntas o problemas, abre un issue en GitHub.
