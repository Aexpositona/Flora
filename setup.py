from setuptools import setup, find_packages

setup(
    name="ludus-herbarum",
    version="1.0.0",
    description="Juego educativo sobre plantas - LUDUS HERBARUM",
    long_description=open("docs/README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Alejandro Expósito Navarro",
    url="https://github.com/Aexpositona/Flora",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pillow>=10.0.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "ludus-herbarum=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="educación botánica plantas juego quiz aprendizaje",
    project_urls={
        "Bug Reports": "https://github.com/Aexpositona/Flora/issues",
        "Source": "https://github.com/Aexpositona/Flora",
        "Documentation": "https://github.com/Aexpositona/Flora/blob/main/docs/README.md",
    },
)
