from setuptools import setup, find_packages
import re


# auto-updating version code stolen from Orbitize which was stolen from RadVel
def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
                       open(project + '/__init__.py').read())
    return result.group(1)

def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

setup(
    name='reflected_light_sim',
    version=get_property('__version__', 'reflected_light_sim'),
    description='reflected-light-sim: a simulator for reflected light of planet',
    url='https://github.com/jlibermann/reflected-light-sim/tree/main',
    author='Josh+Huihao',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ],
    keywords='Reflectance Astronomy',
    install_requires=get_requires()
    )