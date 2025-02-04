from setuptools import setup, find_packages

setup(
    name="kello",  # Sovelluksesi nimi
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kello = kello:main',  # Vaihda 'kello' moduulisi nimeksi ja 'main' funktioksi, joka suoritetaan
        ],
    },
)
