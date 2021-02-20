import os

try:
    os.system('python -m pip install --upgrade pip-21.0.1-py3-none-any.whl')
    os.system('python -m pip install Flask-1.1.2-py2.py3-none-any.whl')
    os.system('python setup.py build')
    os.system('python setup.py install')
    os.system('python -m pip install psutil-5.8.0-cp38-cp38-win32.whl')
except:
    input('Installation failed...')
    
input('Installation succeeded...')