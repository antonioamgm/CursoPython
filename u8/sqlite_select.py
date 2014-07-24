import sqlite3 as dbapi

bbdd = dbapi.connect("bbdd.dat")
print(bbdd)

c=bbdd.cursor()

#c.execute("""drop table empleados""")

c.execute("""create table empleados (dni text,
                    nombre text,
                    departamento text)""")

c.execute("""insert into empleados
                    values ('123345678-A',
                    'Alfonso Ruiz', 
                    'Contabilidad') """)

c.execute("""insert into empleados
                    values ('45678932-C',
                    'Miguel López', 
                    'Contabilidad') """)

bbdd.commit()
c.execute("""select * from empleados 
                        where departamento='Contabilidad'""")

for tupla in c.fetchall(): 
    print(tupla)
