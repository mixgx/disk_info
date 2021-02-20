import os

try:
    os.system('python -m pip install --upgrade pip-21.0.1-py3-none-any.whl')
except:
    input('Installation failed...')

try:
    os.system('python -m pip install psutil')
except:
    try:
        os.system('python -m pip install psutil-5.8.0-cp38-cp38-win32.whl')
    except:
        input('Installation failed...')

try:
    os.system('python -m pip install psutil-5.8.0-cp38-cp38-win32.whl')
except:
    input('Installation failed...')
    
input('Installation succeeded...')