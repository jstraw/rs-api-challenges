#!bin/python

import time

import pyrax
import bootstrap  # bootstrap takes care of auth

cs = pyrax.cloudservers

base_distro = raw_input('Please input a base distribution to use: ')
image_list = [x for x in cs.images.list() if base_distro in x.name]

for x in range(len(image_list)):
    print x, "::", image_list[x].name, "::", image_list[x].id

image = image_list[input("Choose an Image (by number above): ")]
flava = 2
number_of_servers = input('How Many Servers do we need to build? ')
base_name = raw_input('What is the Base Name for the servers? ')

print "Building Servers..."
servers = []
passlist = {}
for x in range(number_of_servers):
    sname = "%s%02d" % (base_name, x+1) 
    s = cs.servers.create(sname, image.id, flava)
    servers.append(s)
    passlist[s.name] = s.adminPass
    print "Boot issued for", sname

servers_online = False
check = []
while not servers_online:
    print "Sleeping 30 seconds..."
    time.sleep(30)
    check = [cs.servers.get(x.id) for x in servers]
    # There may be additional Active/error states, make sure we get
    # all of those states via 'in'
    active = [ x for x in check if 'active' in x.status.lower()]
    error = [ x for x in check if 'error' in x.status.lower()]
    print "Status: %d active %d error of %d" % \
            (len(active), len(error), len(check))
    if len(active) + len(error) == number_of_servers:
        servers_online = True

for x in check:
    print '%s (%s) -- %s -- IP: %s -- password: %s' % \
            (x.name, x.id, x.status, x.networks['public'][0], passlist[x.name])

