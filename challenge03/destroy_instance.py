#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

instance_name = 'pokedex'

print "\nDeleting server:"
conn.delete_server(name_or_id=instance_name)

