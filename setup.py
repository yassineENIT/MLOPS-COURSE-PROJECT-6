from setuptools import setup, find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(    
    name="mlops_project_7",
    version="0.1.0",
    author="Yassine",
    packages=find_packages(),
    install_requires=requirements,
)
