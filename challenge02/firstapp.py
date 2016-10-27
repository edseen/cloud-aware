#! /usr/bin/python

from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

##### Flavors and images #####
images = conn.list_images()
for image in images:
    print(image)
    
flavors =  conn.list_flavors()
for flavor in flavors:
    print(flavor)

# Ubuntu 16.04
#image_id = '94b5d5ff-50b7-4d4f-ac51-da62e7a4909c'
# Ubuntu 14.04
image_id = '95576f28-afed-4b63-93b4-1d07928930da'
image = conn.get_image(image_id)
print(image)

flavor_id = '3'
flavor = conn.get_flavor(flavor_id)
print(flavor)

external_network = '7004a83a-13d3-4dcd-8cf5-52af1ace4cae'

##### Launch an instance #####
#instance_name = 'testing'
#testing_instance = conn.create_server(wait=True, auto_ip=True,
#    name=instance_name,
#    image=image_id,
#    flavor=flavor_id,
#    network=external_network)
#print(testing_instance)

#instances = conn.list_servers()
#for instance in instances:
#    print(instance)

##### Key pair #####
print('Checking for existing SSH keypair...')
keypair_name = 'demokey'
pub_key_file = '/home/edgardo/.ssh/edgardo-HP-dv2500.pub'

if conn.search_keypairs(keypair_name):
    print('Keypair already exists. Skipping import.')
else:
    print('Adding keypair...')
    conn.create_keypair(keypair_name, open(pub_key_file, 'r').read().strip())

for keypair in conn.list_keypairs():
    print(keypair)

##### Network access #####
print('Checking for existing security groups...')
sec_group_name = 'all-in-one'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for all-in-one application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')
    conn.create_security_group_rule(sec_group_name, 22, 22, 'TCP')

conn.search_security_groups(sec_group_name)

##### Userdata #####
ex_userdata = '''#!/usr/bin/env bash

curl -L -s https://git.openstack.org/cgit/openstack/faafo/plain/contrib/install.sh | bash -s -- \
-i faafo -i messaging -r api -r worker -r demo
'''

##### Launch an instance #####
instance_name = 'all-in-one'
testing_instance = conn.create_server(wait=True, auto_ip=False,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    network=external_network,
    key_name=keypair_name,
    security_groups=[sec_group_name],
    userdata=ex_userdata)

instances = conn.list_servers()
for instance in instances:
    print(instance)

#f_ip = conn.available_floating_ip()

#print('The Fractals app will be deployed to http://%s' % f_ip['floating_ip_address'] )

