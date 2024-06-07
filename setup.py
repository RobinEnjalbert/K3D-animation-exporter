from setuptools import setup

PROJECT = 'K3D_animation_exporter'
with open('README.md') as f:
    long_description = f.read()

setup(name=PROJECT,
      version='24.0',
      description='',
      long_description=long_description,
      author='Robin ENJALBERT',
      author_email='robin.enjalbert@inria.fr',
      url='https://github.com/RobinEnjalbert/K3D-animation-exporter',
      packages=[PROJECT],
      package_dir={PROJECT: 'src'},
      install_requires=['k3d'])
