from setuptools import find_packages,setup
from typing import List

def get_requirments()->List[str]:
    """
    This function will return the requirements
    """
    requirement_list:List[str]=[]
    return requirement_list


setup(
    name='sensor',
    version='0.0.1',
    author='Swapnil',
    author_email='swapnil.yande01@gmail.com',
    
    packages=find_packages(),
    install_requires= get_requirments() #['pymongo==4.3.0'],
)

