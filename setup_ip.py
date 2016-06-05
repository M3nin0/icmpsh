#Programa ira compilar o codigo de envio de email com o py2exe
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
        {'script': "send_ip.py"}
    ],
    zipfile=None,
)

shutil.move('dist\\my_program.exe', '.\\my_program.exe')
shutil.rmtree('build')
shutil.rmtree('dist')
