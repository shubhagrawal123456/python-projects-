
from setuptools import setup
setup(name="packageshubh",
version="0.3",
description="This is Shubh's Trial package", 
long_description = "This is long description with Shortcuts",
author="Shubh",
packages=['packageharry'],
install_requires=[])



#Code __init__.py as described/written in the video

class Achha:
    def __init__(self):
        print("Constructor is made")

    def achhafunc(self, number):
        print("This is a function")
        return number
