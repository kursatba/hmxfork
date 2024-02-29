from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.md').read()

REQUIREMENTS = [
    'eth_keys',
    'eth-account',
    'eth-abi',
    'uniswap-universal-router-decoder',
    'web3>6.4.0',
    'simple-multicall',
    'responses',
    'python-dotenv>=1.0.0'
]

setup(
    name='hmx-v2-python',
    version='1.0.0',
    packages=find_packages(),
    package_data={
      'hmx2': ['abis/*.json'],
    },
    description='HMXv2 Python SDK',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/HMXOrg/v2-sdk-python',
    author='HMXOrg',
    license='MIT',
    author_email='kursattek@gmail.com',
    install_requires=REQUIREMENTS,
    keywords='hmx exchange perp dex defi ethereum eth arbitrum',
    classifiers=[
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.11',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)