#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
container_name = 'pokedex'
container = conn.create_container(container_name)

print(conn.list_containers())

pokemons = {'pikachu': 'pokemo-pics/pikachu', 'bulbasaur': 'pokemo-pics/bulbasaur', 'charmander': 'pokemo-pics/charmander', 'miau': 'pokemo-pics/miau', 'squirtle': 'pokemo-pics/squirtle'}

for object_name, file_path in pokemons.items():
	conn.create_object(container=container_name, name=object_name, filename=file_path)

print '\nListing objets in %s' % container_name

print(conn.list_objects(container_name))

