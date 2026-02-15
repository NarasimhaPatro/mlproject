## This file will act like a package where anyone can use our model in there project
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: list[str]

    This function will return the list of requirements
    '''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Narasimha Patro',
    author_email = 'suraj.cse.28@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)