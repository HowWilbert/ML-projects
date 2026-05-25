'''
Use of Setup.py 

Build entire Machine learning Application as a Package,
and Deploy it in pypi. 

From there anybody can install this package and use it(even us).

The folders contaning __init__.py file is treated as a package.
src is our source folder
'''
from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'      # This is a global constant, the -e . makes sure that when the reuqirement.txt is opend it will trigger the setup.py file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
setup(
    name = 'mlproject',
    version='0.0.1',
    author='AnshBire',
    author_email='bireansh1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)