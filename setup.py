'''
setup.py
This file is used to set up the package for distribution.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements from a file and returns them as a list.
    :param file_path: Path to the requirements file.
    :return: List of requirements.
    """
    requirements_lst: List[str] = []

    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
            for line in requirements:
                line = line.strip()
                # Remove comments and empty lines
                if line and line!= '-e .':
                    requirements_lst.append(line)

    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No requirements will be installed.")
    return requirements_lst


setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Elena Lopez Vallejo',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
