#! /usr/bin/python

from shade import *

# Parametros de conexion al cloud
simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

# Imagen
print "Selected image:"
image_id = '95576f28-afed-4b63-93b4-1d07928930da'
image = conn.get_image(image_id)
print(image)

# Tipo de MV
print "\nSelected flavor:"
flavor_id = 'm1.small'
flavor = conn.get_flavor(flavor_id)
print(flavor)

# Red
external_network = '7004a83a-13d3-4dcd-8cf5-52af1ace4cae'

# Key
keypair_name = 'eserna_HP-dv2500'

# Grupo de seguridad
print('Checking for existing security groups...')
sec_group_name = 'admin'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for all-in-one application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')
    conn.create_security_group_rule(sec_group_name, 22, 22, 'TCP')

conn.search_security_groups(sec_group_name)

# Script para despues de ejecucion
ex_userdata = '''#!/usr/bin/env bash
curl -L -s https://raw.githubusercontent.com/edseen/cloud-aware/master/challenge01/init.sh | bash -s --
'''

# Creacion de MV
print "\nServer creation:"
instance_name = 'edseen-01'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    network=external_network,
    security_groups=[sec_group_name],
    key_name=keypair_name,
    userdata=ex_userdata)


print "\nServers in the cloud:"
instances = conn.list_servers()
for instance in instances:
    print(instance)

