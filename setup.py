from setuptools import setup

setup(
        name = "challenges-jstraw",
        version = "0.0.1dev",
        author = "Jason Straw",
        author_email = "jason.straw@rackspace.com",
        license = 'Apache 2.0',

        install_requires = ['pyrax',
                'python-cloudlb'
                    ]
        )

