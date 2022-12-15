from setuptools import find_packages,setup  
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
def get_requirements() ->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        requirement_list = requirements_file.readlines()
        requirement_list=[requirement_namr.replace("/n","") for requirement_name in requirement_list]

        if HYPHEN_E_DON in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


    

setup(
    name="sensor",
    version="0.0.1",
    author= "Atul",
    author_email="anamikagolu1508@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)