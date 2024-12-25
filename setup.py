from setuptools import setup, find_packages

setup(
    name="scribe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Your project dependencies
        # "elasticsearch>=7.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.0.0",
        ]
    },
)