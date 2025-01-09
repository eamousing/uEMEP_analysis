from setuptools import setup, find_packages

setup(
    name="uEMEP_analysis",
    version="0.1.0",
    author="Erik Askov Mousing",
    author_email="erik.a.mousing@met.no",
    description="A collection of scripts for analyzing output from the uEMEP model",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/emousing/uEMEP_analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
        ],
    },
)
