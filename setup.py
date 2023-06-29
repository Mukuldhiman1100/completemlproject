## Its purpose is to build ML applicatioan as a package

from setuptools import find_packages,setup
from typing1 import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","")for req in requirements]

        # it is used so whenever the requirements.txt install the packages
        # it will not run the hyphen e dot 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='complete ml project',
    version='0.0.1',
    author='Mukul',
    author_email='mukuldhiman1100@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)