from setuptools import setup, find_packages

setup(
    name="kello", 
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kello = kello:main', 
        ],
    },
    extras_require={
        'tkinter': [
            "macOS: brew install python-tk", 
            "Windows: Asenna Python uudelleen ja varmista, että tkinter on mukana"
        ]
    },
)
