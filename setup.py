from setuptools import find_packages, setup


requirements = [
    'setuptools',
    'numpy',
    'scikit-image',
]


setup(
    name='trænsforms',
    version='0.1.0',
    license='MIT',
    author='Holim Lim',
    author_email='ihl7029@europa.snu.ac.kr',
    url='https://github.com/Holim0711/pytorch-transforms',
    description='Data converter for pytorch',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)

