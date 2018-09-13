import py_compile
import marshal

def compileCredentials():
    py_compile.compile('Credentials.py', 'Credentials.pyc')

def getCredentials():
    s = open('Credentials.pyc', 'rb')
    s.seek(12)
    code_object = marshal.load(s)
    exec(code_object)
    return password()


