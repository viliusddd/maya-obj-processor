

from sys import argv
from os.path import isfile, isdir, join
from os import walk

class Obj(object):
    def __init__(self, path):
        self.path = path

    def walk(self):
        filesObj = []
        filesAll = []

        if isdir(self.path):
            for root, dirs, files in walk(self.path):
                for item in files:
                    filesAll.append(join(root, item))
            for item in filesAll:
                if item.endswith('.obj'):
                    filesObj.append(item)
            return list(filesObj)

        elif isfile(self.path):
            if self.path.endswith('.obj'):
                return self.path

    def open_maya(self):
        #open maya and run certain script in maya batch mode
        pass

    def 

obj = Obj(argv[1])

print(obj.walk())