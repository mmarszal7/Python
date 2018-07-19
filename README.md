# Python notes
#### Some pip/conda commands:
**yolk3k** - Package containing command-line tool for quering about pip package informations like version, authors etc.
- pip -h 
- pip freeze > requirements.txt
- pip install requirements.txt
- conda create -n django python=3.6
- conda env list
- conda env remove -n envName
- conda env export --file environment.yml
- conda env create -f environment.yml
- yolk -V django 

#### Code/project structure:
**Package** - folder with source code files and \_\_init\_\_.py file </br>
**Module** - each source code file - often with if \_\_name__ == "\_\_main\_\_": function
```python
README.md
LICENSE
docs/config.py
docs/documentation.md

setup.py	# package instalation file - here you define solution details e.g. version, author, manufacturer etc.
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

## Django:
**Installation and first run:**
``` python
pip install Django==1.11.2
django-admin startproject mysite
django-admin.py startapp api
// Optional step
python manage.py createsuperuser --email admin@example.com --username admin
``` 
**Running app:**
``` 
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver
```

## Basics:
**Strings:**
```python
name[1:len(name)]   
len(name),          
name.upper()
str(age)            
int(age)            
print("Name: %s, Lastname: %s" % (name, lastName))
```
**Dates:**
```python
from datetime import datetime
now = datetime.now()
print '%s/%s/%s’ % (now.year, now.month, now.day,)
```
**Lists:**
```python
names = list() # names = []
name = names[2:3]
names.append()
names.index(x)
names.insert(x,y)
names.sort()
names.remove()
for name in names: 
    pass
```

**Dicrtionaries:**
```python
dict = {‘A’ : 10, ‘B‘: 15, ‘C’ : 20}
dict(‘A’) = 10
del dict[‘B’]
```
