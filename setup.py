from setuptools import setup

setup(
    name="dummy-framework",
    version = "0.1.0",
    description="Test framework to perform dummy tests.",
    install_requires=[
        'pytest>=6.2.5',
        'pytest-html>=3.1.1',
        'pytest-cov>=3.0.0',
    ],
    extras_require={},
    author='Dummy Inc.',
)
