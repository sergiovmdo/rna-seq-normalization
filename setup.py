from setuptools import setup, find_packages

setup(
    name='rna-seq-normalization',
    version='0.1.0',
    description='My Python Package',
    author='Sergio Vazquez Montes de Oca',
    author_email='sergiovazquezmontesdeoca@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['rna-seq', 'rna', 'tpm', 'normalization', 'rpkm', 'cpm', 'rna-sequencing', 'statistics', 'bioinformatics'
              'data analysis', 'data science'],
    install_requires=[],
    python_requires='>=3.6',
)
