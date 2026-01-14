from setuptools import setup, find_packages

setup(
    name="mapa-de-profundidades",
    version="0.1.0",
    description="Análisis de las profundidades de compra - Order Book Depth Analysis",
    author="luciagl18",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "requests>=2.26.0",
        "python-dotenv>=0.19.0",
    ],
    python_requires=">=3.8",
)
