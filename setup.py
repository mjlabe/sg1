from setuptools import setup

setup(
    name='sg1',
    version='0.1.1',
    description='A stupid, simple, static site generator',
    url='https://github.com/mjlabe/sg1',
    author='Marc LaBelle',
    packages=['sg1', 'sg1.helpers'],
    entry_points={
        'console_scripts': ['sg1=sg1.manage:main'],
    },
    python_requires='>=3.6, <4',
    install_requires=['Jinja2>=2.11.3', 'MarkupSafe>=1.1.1'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)
