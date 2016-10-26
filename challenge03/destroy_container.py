#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

container_name = 'pokedex'

for object in conn.list_objects(container_name):
	print('Good bye %s!' % object['name'])
	conn.delete_object(container_name, object['name'])

conn.delete_container(container_name)
