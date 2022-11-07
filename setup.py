from setuptools import setup, find_packages

setup(
  name = 'nniot',
  packages = find_packages(exclude=['examples']),
  version = '0.1.0',
  license='MIT',
  description = 'Optimizing neural networks for electrical motor tasks for Industrial IoTs- Pytorch',
  author = 'Sagar Verma',
  author_email = 'sagar15056@iiitd.ac.in',
  url = 'https://github.com/sagarverma/nn-for-iiot',
  keywords = [
    'artificial intelligence',
    'motors',
    'iot',
    'time-series'
  ],
  install_requires=[
    'einops>=0.4.1',
    # 'torch==1.8.1',
    'jupyterlab',
    'matplotlib==3.3.2',
    'scipy==1.8.0',
    'scikit-learn',
    'tqdm',
    'pandas',
    'tensorboardx',
    'tensorboard',
    'mat73',
    'sympy'
  ],
  setup_requires=[
    'pytest-runner',
  ],
  tests_require=[
    'pytest'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8.5',
  ],
)
