from setuptools import setup, find_packages

setup(
    name="event_generator",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'openai',
        'kafka-python'
    ],
    entry_points={
        'console_scripts': [
            'event_generator = event_generator.main:main_loop',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
