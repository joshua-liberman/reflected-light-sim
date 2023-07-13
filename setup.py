from setuptools import setup, find_packages

def get_requires():
    reqs = []
    for line in open('requirements.txt', 'r').readlines():
        reqs.append(line)
    return reqs

setup(
    name='reflected_light_sim',
    version='0.1',
    description='reflected_light_sim: a simulator for reflected light of planet',
    url='https://github.com/jlibermann/reflected-light-sim/tree/main',
    author='Josh+Huihao',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
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
    install_requires=get_requires()
    )