from yaspin import yaspin
import time
from random import randint

from glob import glob
import os

def load():
    with yaspin(text='Loading', color='magenta') as spinner:
        files = [os.path.basename(f) for f in glob('./*.epub')]    
        spinner.ok("✅ ")
        return files

def read_manifest(file):
    
    
