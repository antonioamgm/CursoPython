import sqlite3 as dbapi


bbdd= dbapi.connect("bbdd.dat")

c = bbdd.cursor()
#c.execute("""create table empleados(dni text, nombre text, departamento text)""")
c.execute("""insert into empleados values('123345678-A', 'Alfonso Ruiz', 'Contabilidad')""")
bbdd.commit()



bbdd.close()
