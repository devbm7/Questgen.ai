from distutils.core import setup

setup(name='Questgen',
      version='1.0.1',
      description='Question generator from any text',
      author='Questgen contributors',
      author_email='vaibhavtiwarifu@gmail.com',
      packages=['Questgen', 'Questgen.encoding', 'Questgen.mcq'],
      url="https://github.com/ramsrigouthamg/Questgen.ai",
      install_requires=[
            'torch',
            'transformers==4.29.2',
            'sense2vec==2.0.2',
            'strsim==0.0.3',
            'six==1.16.0',
            'networkx==3.1',
            'numpy==1.22.4',
            'scipy',
            'scikit-learn',
            'unidecode',
            'future',
            'joblib',
            'pytz',
            'python-dateutil',
            'flashtext',
            'pandas',
            'sentencepiece'
      ],
      package_data={'Questgen': ['questgen.py', 'mcq.py', 'train_gpu.py', 'encoding.py']}
      )
