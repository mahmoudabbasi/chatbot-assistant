from setuptools import setup, find_packages

setup(
    name="chatbot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "numpy",
        "tensorflow"
    ],
    entry_points={
        "console_scripts": [
            "chatbot=chatbot.assistant:main",
        ]
    },
    include_package_data=True,
    package_data={
        "": ["*.json"],
    },
    author="Mahmoud Abbasi",
    author_email="mahmoud.abbasi.m@gmail.com",
    description="A basic chatbot package",
    keywords="chatbot machine learning",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
