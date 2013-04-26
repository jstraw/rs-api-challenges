import pyrax
import os.path

creds = os.path.expanduser('~/.rackspace_cloud_credentials')
pyrax.set_credential_file(creds)



