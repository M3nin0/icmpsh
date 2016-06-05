'''
Este arquivo apenas e utilizado no momento de compilar o pass_string, este que deve ser feito
antes do envio ao alvo
Ira fazer todas as dependencias do py2exe, para que o codigo gerado consiga compilar os demais codigos gerados posteriormente
'''
import sys
import py2exe
from distutils.core import setup
import shutil

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True}
    },
    console=[
        {'script': "pass_string.py"}
    ],
    zipfile=None,
)

shutil.move('dist\\my_program.exe', '.\\my_program.exe')
shutil.rmtree('build')
shutil.rmtree('dist')
