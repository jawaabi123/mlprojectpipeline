from setuptools import find_packages,setup

#'-e .' is given in the requirements.txt to indicate the presence of setup.py file and that will build the project package
def get_requirements(file_path:str):
    """
    this function will return the list of requirements for the project
    """
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
        
        return requirements

setup(
name='mlprojectpipeline',
version='0.0.1',
author='jawahar abishek',
author_email='kjawharabishek@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)