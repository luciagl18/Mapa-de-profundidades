"""
Main application script
Script principal para ejecutar el análisis de profundidad
"""

import argparse
import sys
from pathlib import Path

from mapa_profundidades import DataLoader, DepthAnalyzer, DepthVisualizer


def main():
    """Función principal del programa."""
    parser = argparse.ArgumentParser(
        description='Análisis de profundidad del libro de órdenes'
    )
    parser.add_argument(
        'input_file',
        type=str,
        help='Archivo de entrada con datos del libro de órdenes (CSV o JSON)'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='Directorio de salida para los resultados'
    )
    parser.add_argument(
        '--levels',
        type=int,
        default=10,
        help='Número de niveles de precio a analizar'
    )
    parser.add_argument(
        '--visualize',
        action='store_true',
        help='Generar visualizaciones'
    )
    
    args = parser.parse_args()
    
    # Cargar datos
    print(f"Cargando datos desde {args.input_file}...")
    loader = DataLoader()
    
    file_path = Path(args.input_file)
    if file_path.suffix == '.csv':
        data = loader.load_from_csv(args.input_file)
    elif file_path.suffix == '.json':
        import json
        with open(args.input_file, 'r') as f:
            order_book = json.load(f)
        data = loader.parse_order_book(order_book)
    else:
        print(f"Error: Formato de archivo no soportado '{file_path.suffix}'")
        sys.exit(1)
    
    print(f"Datos cargados: {len(data)} órdenes")
    
    # Analizar profundidad
    print("\nAnalizando profundidad del mercado...")
    analyzer = DepthAnalyzer(data)
    
    depth_metrics = analyzer.calculate_depth(price_levels=args.levels)
    spread_metrics = analyzer.calculate_spread()
    liquidity_metrics = analyzer.analyze_liquidity()
    
    # Mostrar resultados
    print("\n=== MÉTRICAS DE PROFUNDIDAD ===")
    print(f"Profundidad de Bids: {depth_metrics['bid_depth']:.2f}")
    print(f"Profundidad de Asks: {depth_metrics['ask_depth']:.2f}")
    print(f"Profundidad Total: {depth_metrics['total_depth']:.2f}")
    print(f"Ratio Bid/Ask: {depth_metrics['bid_ask_ratio']:.2f}")
    print(f"Desequilibrio de Profundidad: {depth_metrics['depth_imbalance']:.2%}")
    
    print("\n=== MÉTRICAS DE SPREAD ===")
    print(f"Mejor Bid: ${spread_metrics['best_bid']:.2f}")
    print(f"Mejor Ask: ${spread_metrics['best_ask']:.2f}")
    print(f"Spread: ${spread_metrics['spread']:.2f}")
    print(f"Precio Medio: ${spread_metrics['mid_price']:.2f}")
    print(f"Spread %: {spread_metrics['spread_percentage']:.2%}")
    
    print("\n=== MÉTRICAS DE LIQUIDEZ ===")
    print(f"Liquidez de Bids: {liquidity_metrics['bid_liquidity']:.2f}")
    print(f"Liquidez de Asks: {liquidity_metrics['ask_liquidity']:.2f}")
    print(f"Liquidez Total: {liquidity_metrics['total_liquidity']:.2f}")
    print(f"Órdenes de Bid: {liquidity_metrics['bid_orders']}")
    print(f"Órdenes de Ask: {liquidity_metrics['ask_orders']}")
    
    # Generar visualizaciones si se solicita
    if args.visualize:
        print("\nGenerando visualizaciones...")
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        visualizer = DepthVisualizer()
        
        # Gráfico de profundidad
        fig = visualizer.plot_depth_chart(data)
        visualizer.save_figure(output_dir / 'depth_chart.png')
        print(f"Guardado: {output_dir / 'depth_chart.png'}")
        
        # Distribución de órdenes
        fig = visualizer.plot_order_distribution(data)
        fig.savefig(output_dir / 'order_distribution.png', dpi=300, bbox_inches='tight')
        print(f"Guardado: {output_dir / 'order_distribution.png'}")
        
        # Niveles de precio
        fig = visualizer.plot_price_levels(data)
        fig.savefig(output_dir / 'price_levels.png', dpi=300, bbox_inches='tight')
        print(f"Guardado: {output_dir / 'price_levels.png'}")
        
        print("\nVisualizaciones completadas.")
    
    print("\nAnálisis completado.")


if __name__ == '__main__':
    main()
