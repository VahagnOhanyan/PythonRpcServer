from distutils.core import setup
import py2exe

setup(
    console=['main.py'],
    packages=['code', 'config'],
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True
        }
    },
    zipfile=None
)
