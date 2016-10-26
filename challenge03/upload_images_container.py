#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

# Crear contenedor
container_name = 'pokedex'
container = conn.create_container(container_name)

# Cargar imagenes al contenedor
pokemons = {'bulbasaur': 'pokemo-pics/bulbasaur.png', 'charmander': 'pokemo-pics/charmander.png', 'miau': 'pokemo-pics/miau.png', 'pikachu': 'pokemo-pics/pikachu.png', 'squirtle': 'pokemo-pics/squirtle.png'}

for object_name, file_path in pokemons.items():
	conn.create_object(container=container_name, name=object_name, filename=file_path)

