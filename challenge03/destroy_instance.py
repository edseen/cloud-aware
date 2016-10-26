#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
instance_name = 'pokedex'

print "\nDeleting server:"
conn.delete_server(name_or_id=instance_name)

container_name = 'pokedex'

print '\nDeleting objects in %s' % container_name
for object in conn.list_objects(container_name):
	print('Good bye %s!' % object['name'])
	conn.delete_object(container_name, object['name'])

conn.delete_container(container_name)
