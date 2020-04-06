#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

import os
import sys
import imp

############################################################
from setuptools import find_packages, setup, convert_path

############################################################
# Version
version = imp.load_source(
    'cbrain.__init__', os.path.join('cbrain', '__init__.py')).__version__

# Default portal
portal_url='https://cBrain.io'

# Read description (TBD: should add short description!)
with open(convert_path('./README.md')) as f:
    long_readme = f.read()

# Package description
setup(
    name='cbrain',

    author="Grigori Fursin",
    author_email="Grigori.Fursin@cTuning.org",

    version=version,

    description="cBrian.io client to exchange reusable computational components and workflows",

    license="Apache Software License (Apache 2.0)",

    long_description_content_type='text/markdown',
    long_description=long_readme,

    url=portal_url,

    python_requires=">=2.7",

    packages=find_packages(exclude=["tests*", "docs*"]),
    package_data={"cbrain":['static/*']},

    include_package_data=True,

    install_requires=[
      'click>=7.0',
      'ck',
      'requests',
      'virtualenv'
    ],

    entry_points={
      "console_scripts": 
        [
         "cr = cbrain.main:cli",
         "cb = cbrain.main:cli"
        ]
    },

    zip_safe=False,

    keywords="reusable computational components, portable workflows, reproducibility, collaborative experiments, portability, dependencies, workflows, automation, pipelines, data pipelines, computer systems, data science, collective knowledge",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research"
       ],
)

###########################################################
# Get release notes 
import cbrain.comm
r=cbrain.comm.send({'config':{'server_url':portal_url+'/api/v1/?'},
                    'action':'event', 
                    'dict':{'type':'get-client-release-notes','version':version}})
notes=r.get('notes','')
if notes!='':
   print ('*********************************************************************')
   print ('Release notes:')
   print ('')
   print (notes)
   print ('*********************************************************************')
