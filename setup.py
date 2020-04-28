#
# Developer(s): Grigori Fursin
#               Herve Guillou
#

import os
import sys
import imp

############################################################
from setuptools import find_packages, setup, convert_path

try:
    from io import open
except ImportError:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from setuptools import convert_path
except ImportError:
    from distutils.util import convert_path

try:
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install

try:
   from setuptools.command.install_scripts import install_scripts
except ImportError:
    from distutils.command.install_scripts import install_scripts

try:
   from setuptools.command.install_lib import install_lib
except ImportError:
    from distutils.command.install_lib import install_lib

from distutils.sysconfig import get_python_lib

############################################################
# Version
version = imp.load_source(
    'cbench.__init__', os.path.join('cbench', '__init__.py')).__version__

# Default portal
portal_url='https://cKnowledge.io'

dir_install_script=""

############################################################
class custom_install(install):
    def run(self):
        global dir_install_script

        install.run(self)

        # Check if detected script directory
        if dir_install_script!="" and os.path.isdir(dir_install_script):
           # Check which python interpreter is used
           python_bin=sys.executable
           real_python_bin=os.path.abspath(python_bin)

           if os.path.isfile(python_bin):
              # Attempt to write to $SCRIPTS/ck-python.cfg
              file_type='wb'
              if sys.version_info[0]>2:
                 file_type='w'

              p=os.path.join(dir_install_script, 'cb-python.cfg')

              try:
                 with open(p, file_type) as f:
                    f.write(python_bin+'\n')

                 print ('')
                 print ("Writing cBench python executable ("+python_bin+") to "+p)
                 print ('')
              except Exception as e: 
                 print ("warning: can\'t write info about cBench python executable to "+p+" ("+format(e)+")")
                 pass

        # Check update 
        import cbench.comm_min
        r=cbench.comm_min.send({'url':portal_url+'/api/v1/?',
                                'action':'event', 
                                'dict':{'type':'check-cbench-update','version':version}})
        notes=r.get('notes','')
        if notes!='':
           print (notes)

############################################################
class custom_install_scripts(install_scripts):
   def run(self):
       global dir_install_script

       install_scripts.run(self)

       dir_install_script=os.path.abspath(self.install_dir)

       if dir_install_script!=None and dir_install_script!="" and os.path.isdir(dir_install_script):
          print ('')
          print ("Detected script installation directory: "+dir_install_script)
          print ('')

       return


############################################################
setup(
    name='cbench',

    author="Grigori Fursin",
    author_email="Grigori.Fursin@cTuning.org",

    version=version,

    description="A cross-platform client to perform collaborative and reproducible benchmarking, optimization and co-design of software and hardware for emerging workloads (AI, ML, quantum, IoT) via the open cKnowledge.io portal",

    license="Apache Software License (Apache 2.0)",

    long_description=open(convert_path('./README.md'), encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url=portal_url,

    python_requires=">=2.7",

    packages=find_packages(exclude=["tests*", "docs*"]),
    package_data={"cbench":['static/*']},

    include_package_data=True,

    cmdclass={
     'install': custom_install, 
     'install_scripts': custom_install_scripts
    },

    install_requires=[
      'click>=7.0',
      'ck',
      'requests',
      'virtualenv'
    ],

    entry_points={
      "console_scripts": 
        [
         "cr = cbench.main:cli",
         "cb = cbench.main:cli",
         "cbench = cbench.main:cli"
        ]
    },

    zip_safe=False,

    keywords="reproducible benchmarking, customizable benchmarking, portable workflows, reusable computational components, reproducibility, collaborative experiments, automation, optimization, co-design, collective knowledge",

    install_requires=['requests'],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research"
        "Environment :: Console",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: System",
        "Topic :: System :: Benchmark",
        "Topic :: Education",
        "Topic :: Utilities"
       ],
)
