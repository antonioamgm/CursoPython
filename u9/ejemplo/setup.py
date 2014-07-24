from distutils.core import setup
import py2exe
setup(name="Ejemplo Python de aplicación .exe",
	version="0.1",
	description="Ejemplo de ejecución de una aplicación Python con un fichero .exe",
	author="José Luis Merino",
	author_email="jlmerdiez@gmail.com",
	url="www.anexpertforyou.com",
	license="GPL",
	scripts=["ejemplo.py"],
	console=["ejemplo.py"],
	platforms=["Win", "Mac", "Linux"],
	long_description = """Un texto largo iría aquí.""",
	options={"py2exe":{"bundle_files":1}},
	zipfile=None
)