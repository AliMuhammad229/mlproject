from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."

def get_requirments(filepath:str)->List[str]:
    '''
    this fn will return the list of requirements
    '''
    requirements = []
    with open(filepath) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", " ")for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='AliMuhammad',
    author_email='aliqasim.am7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)