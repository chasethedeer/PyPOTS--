import os

from setuptools import find_packages
from setuptools import setup

from pypots import __version__

with open("./README.md", encoding="utf-8") as f:
    README = f.read()

with open(
    os.path.join("requirements", "requirements.txt"),
    encoding="utf-8",
) as f:
    requirements = f.read().splitlines()

setup(
    name="pypots",
    version=__version__,
    description="A Python Toolbox for Machine Learning on Partially-Observed Time Series",
    long_description=README,
    long_description_content_type="text/markdown",
    license="BSD-3-Clause",
    author="Wenjie Du",
    author_email="wenjay.du@gmail.com",
    url="https://pypots.com/",
    project_urls={
        "Documentation": "https://docs.pypots.com/",
        "Source": "https://github.com/WenjieDu/PyPOTS/",
        "Tracker": "https://github.com/WenjieDu/PyPOTS/issues/",
        "Download": "https://github.com/WenjieDu/PyPOTS/archive/main.zip",
    },
    keywords=[
        "data science",
        "data mining",
        "neural networks",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "time-series analysis",
        "time series",
        "imputation",
        "interpolation",
        "classification",
        "clustering",
        "forecasting",
        "partially observed",
        "irregular sampled",
        "partially-observed time series",
        "incomplete time series",
        "missing data",
        "missing values",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.8.0",
    setup_requires=["setuptools>=38.6.0"],
    entry_points={"console_scripts": ["pypots-cli=pypots.cli.pypots_cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
