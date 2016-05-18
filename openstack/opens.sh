#!/usr/bin/python
#
#  libcloud Apache OpenStack

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import libcloud.security
#libcloud.security.VERIFY_SSL_CERT = False


auth_username = 'bsv'
auth_password = '1q2w3e'
auth_url = 'http://192.168.103.191:5000/v2.0/tokens'
project_name = 'BSV'
region_name = ''

provider = get_driver(Provider.OPENSTACK)
conn = provider(auth_username,
                auth_password,
                ex_force_auth_url=auth_url,
                ex_force_auth_version='2.0_password',
                ex_tenant_name=project_name,
                ex_force_service_region=region_name)

images = conn.list_images()
for image in images:
    print image

print "\n Flafor"
flavors = conn.list_sizes()
for flavor in flavors:
    print(flavor)

flavor_id = '1'
flavor = conn.ex_get_size(flavor_id)
print "\n \n \n "
print(flavor)

#networks = conn.list_networks() print networks

#net = ['92ea6df6-98bf-4240-814f-bbd64e81d9bd']

#net_public = conn.ex_create_network('private' , '10.0.0.0/24')
nets = conn.ex_list_networks()
print "\n Nets: "
print nets


#instance_name = 'InstanceFirstTest'
#testing_instance = conn.create_node(name=instance_name, image=images[8], size=flavors[0], networks=[nets[1]])
#print(testing_instance)
