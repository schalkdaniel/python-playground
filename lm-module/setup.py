from setuptools import setup

setup(
    name='lm',
    version='0.1',
    description='A module that behaves similar to Rs lm',
    author='D. S.',
    author_email='ds@foo.example',
    packages=['lm'],  #same as name
    install_requires=['numpy', 'pandas'],
)
