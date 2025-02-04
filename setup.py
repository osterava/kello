from setuptools import setup, find_packages

setup(
    name="kello",  # Sovelluksesi nimi
    version="0.1",
    packages=find_packages(),
    install_requires=[  # Listaa kaikki riippuvuudet täällä
        'tkinter',  # Esimerkiksi tkinter
    ],
    entry_points={
        'console_scripts': [
            'kello = kello:main',  # Vaihda 'kello' moduulisi nimeksi ja 'main' funktioksi, joka suoritetaan
        ],
    },
)
