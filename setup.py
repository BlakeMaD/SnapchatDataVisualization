from distutils.core import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='Snapchat_Visualization',
    version='0.1.0',
    packages=['Snapviz'],
    url='',
    long_description=long_description,
    license='MIT',
    author='Blake Dukes',
    author_email='dukes4@purdue.edu',
    install_requires=['calplot', 'pandas', 'seaborn'], #external packages as dependencies
    description='Data Visualization for snapchat data'
)