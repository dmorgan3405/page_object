from setuptools import setup, find_packages

setup(
    name="page_object",
    version="0.0.7",
    description='PageObject pattern python implementation',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=[
        'pyvirtualdisplay==0.2',
        'selenium==3.0.2'
    ]
)
