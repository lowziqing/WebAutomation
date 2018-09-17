import py_compile


class Compiler:
    def compileCredentials(self):
        py_compile.compile('SeleniumScript/Credentials.py', 'SeleniumScript/Credentials.pyc')





