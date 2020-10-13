import setuptools
from semilla_moneda import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()

CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Internet",
    "Topic :: Utilities",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

CONSOLE_SCRIPTS = ["semilla-moneda=semilla_moneda.semilla_moneda:main"]
PACKAGE_DATA = {'semilla-moneda': ['*.txt']}

setuptools.setup(
    name="semilla-moneda",
    version=__version__,
    author="Lunaticoin",
    author_email="lunaticoin@protonmail.com",
    description="Entropia generada con una moneda",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lunaticoin/semilla_moneda",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data=PACKAGE_DATA,
    classifiers=CLASSIFIERS,
    python_requires=">=3.6",
    entry_points={"console_scripts": CONSOLE_SCRIPTS},
)

