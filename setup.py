from setuptools import setup, find_packages

setup(
    name='object-get',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/Lete114/python-object-get',
    license='MIT',
    author='Lete114',
    author_email='mylete114@gmail.com',
    description='Use "." to get the value of a JSON object. Just like JavaScripthat gets the value of an object',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
