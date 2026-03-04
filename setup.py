from setuptools import setup

setup(
    name="algo-arena",
    version="0.1.0",
    py_modules=["arena_cli"],
    entry_points={
        "console_scripts": [
            "arena=arena_cli:main"
        ]
    },
    description="A competitive programming CLI product for quick bootstrapping and C/Python benchmarking.",
    author="Gencer Sarp Mert"
)
