# Ver http://pymotw.com/2/shelve/ y adaptarlo a Python 3

import shelve

s = shelve.open('datos.db')
s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
s.close()

s = shelve.open('datos.db')
existing = s['key1']
s.close()
print(existing)
