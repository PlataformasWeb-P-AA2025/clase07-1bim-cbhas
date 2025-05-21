from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Sacar las matriculas con su estudiante y módulo
# matriculas = session.query(Matricula).all()


# for m in matriculas:
#     print(m, m.estudiante, m.modulo)

# Se consulta la tabla matricula como inicio, para de ahi hacer una union co la tabla estudiante 
# y modulo para de ahi filtrar los estudiantes que solamente tenga el nombre 'Tony'
modulos = session.query(Matricula).join(Estudiante).join(Modulo)\
    .filter(Estudiante.nombre == 'Tony').all()

# Se recorre la lista de matrículas filtradas para imprimir el nombre del módulo y el nombre completo del estudiante
for m in modulos:
    print(f"{m.modulo.nombre} - {m.estudiante.nombre} {m.estudiante.apellido}")
