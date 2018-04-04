# Python notes
#### Some pip/conda commands:
**yolk3k** - Package containing command-line tool for quering about pip package informations like version, authors etc.
- pip -h 
- pip install requirements.txt
- conda env list
- conda env remove -n envName
- yolk -V django 

#### Code/project structure:
**Package** - folder with source code files and \_\_init\_\_.py file
**Module** - each source code file - often with if \_\_name__ == "\_\_main\_\_": function
```python
README.md
LICENSE
docs/config.py
docs/documentation.md

setup.py			# package instalation file - here you define solution details e.g. version, author, manufacturer etc.
requirements.txt    # package list - package.json equivalent
makefile            # buildfile - definitions of operations like building, testing, cleaning etc.

sample_package/__init__.py
sample_package/core.py
sample_package/helpers.py
tests/test_basic.py
tests/test_advanced.py
```
#### Keras installation:
As always check installtion page first!

```python
conda env list
conda create -n keras pip python=3.5 
activate keras
pip install --ignore-installed --upgrade tensorflow #tensorflow==1.4.0
pip install keras

pip install ipykernel
ipython kernel install --user --name=keras
jupyter notebook
# Kernel > Change kernel > keras
```