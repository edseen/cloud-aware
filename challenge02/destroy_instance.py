#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
#instance_name = 'testing'
instance_name = 'all-in-one'

conn.delete_server(name_or_id=instance_name)
