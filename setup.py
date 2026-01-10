# building our model as package itself so that others can use it easily
# what pipi 
# from setuptools import find_packages, setup
# from typing import List


from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    """
    with open(file_path, 'r') as f:
        requirements = [req.strip() for req in f.readlines()]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements


# setup(
#     name='mlproject',
#     version='0.0.1',
#     author="Nikhil Rathaur",
#     author_email="rathaurd822@gmail.com",
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )


setup(
    name = 'mlproject',
    version= '0.0.1',
    author="Nikhi Rathaur",
    author_email= "rathaurd822@gmail.com",
    packages= find_packages(),                        # this will take src/__init__.py and helps us out to import the file here
    # install_requires = ['pandas', 'numpy', 'seaborn']
    install_requires = get_requirements('requirements.txt')
)