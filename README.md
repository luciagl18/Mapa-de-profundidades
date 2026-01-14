# Mapa de Profundidades

Análisis de las profundidades de compra - Order Book Depth Analysis

## Descripción

Mapa de Profundidades es una herramienta de análisis para visualizar y analizar la profundidad del libro de órdenes en mercados financieros. Proporciona métricas detalladas sobre liquidez, spread, y distribución de órdenes de compra y venta.

## Características

- 📊 **Análisis de Profundidad**: Calcula métricas de profundidad del mercado a múltiples niveles de precio
- 📈 **Visualizaciones**: Genera gráficos interactivos del libro de órdenes
- 💹 **Métricas de Spread**: Calcula y analiza el spread bid-ask
- 💰 **Análisis de Liquidez**: Evalúa la liquidez disponible a diferentes distancias de precio
- 🔄 **Múltiples Formatos**: Soporta datos en CSV y JSON

## Instalación

### Requisitos

- Python 3.8 o superior
- pip

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

O instalar el paquete en modo desarrollo:

```bash
pip install -e .
```

## Uso

### Uso Básico

```bash
python src/main.py data/example_orderbook.csv
```

### Uso con Visualizaciones

```bash
python src/main.py data/example_orderbook.csv --visualize
```

### Opciones Avanzadas

```bash
python src/main.py data/example_orderbook.json \
    --output results \
    --levels 20 \
    --visualize
```

### Argumentos de Línea de Comandos

- `input_file`: Archivo de entrada con datos del libro de órdenes (requerido)
- `--output`: Directorio de salida para resultados (default: `output`)
- `--levels`: Número de niveles de precio a analizar (default: `10`)
- `--visualize`: Generar visualizaciones gráficas

## Uso como Biblioteca

```python
from mapa_profundidades import DataLoader, DepthAnalyzer, DepthVisualizer

# Cargar datos
loader = DataLoader()
data = loader.load_from_csv('data/example_orderbook.csv')

# Analizar profundidad
analyzer = DepthAnalyzer(data)
depth_metrics = analyzer.calculate_depth(price_levels=10)
spread_metrics = analyzer.calculate_spread()
liquidity_metrics = analyzer.analyze_liquidity()

# Visualizar
visualizer = DepthVisualizer()
fig = visualizer.plot_depth_chart(data)
visualizer.save_figure('depth_chart.png')
```

## Formato de Datos

### CSV

```csv
price,volume,side
50000.00,1.5,bid
50001.00,1.6,ask
```

### JSON

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

## Estructura del Proyecto

```
Mapa-de-profundidades/
├── src/
│   ├── mapa_profundidades/
│   │   ├── __init__.py
│   │   ├── data_loader.py      # Carga de datos
│   │   ├── depth_analyzer.py   # Análisis de profundidad
│   │   └── visualizer.py       # Visualizaciones
│   └── main.py                 # Script principal
├── tests/                      # Tests unitarios
├── data/                       # Datos de ejemplo
├── config/                     # Configuración
├── requirements.txt           # Dependencias
├── setup.py                   # Instalación del paquete
└── README.md                  # Este archivo
```

## Pruebas

Ejecutar todos los tests:

```bash
python -m pytest tests/
```

O ejecutar tests específicos:

```bash
python -m unittest tests.test_data_loader
python -m unittest tests.test_depth_analyzer
python -m unittest tests.test_visualizer
```

## Métricas Calculadas

### Profundidad
- **Bid Depth**: Volumen total de órdenes de compra
- **Ask Depth**: Volumen total de órdenes de venta
- **Total Depth**: Profundidad total del mercado
- **Bid/Ask Ratio**: Ratio entre compras y ventas
- **Depth Imbalance**: Desequilibrio de profundidad

### Spread
- **Best Bid**: Mejor precio de compra
- **Best Ask**: Mejor precio de venta
- **Spread**: Diferencia entre bid y ask
- **Mid Price**: Precio medio del mercado
- **Spread Percentage**: Spread como porcentaje

### Liquidez
- **Bid Liquidity**: Liquidez disponible en compras
- **Ask Liquidity**: Liquidez disponible en ventas
- **Total Liquidity**: Liquidez total del mercado
- **Order Counts**: Número de órdenes por lado

## Configuración

Copiar `.env.example` a `.env` y ajustar los valores según sea necesario:

```bash
cp .env.example .env
```

## Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto.

## Autor

**luciagl18**

## Soporte

Para reportar problemas o solicitar características, por favor abre un issue en GitHub.
