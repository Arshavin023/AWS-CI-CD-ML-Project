from setuptools import find_packages,setup
from typing import List

HYPHEN_E_NOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #this reads each line from requirements.txt
        requirements=[req.replace("\n","") for req in requirements] #this replace '\n' from step above
        if HYPHEN_E_NOT in requirements:
            requirements.remove(HYPHEN_E_NOT)
    
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Uche Nnodim',
    author_email='uchejudennodim@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)