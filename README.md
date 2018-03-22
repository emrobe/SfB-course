# SfB-course
Deployment implementation for SfB related courses (Use with Ubuntu 16.04)

TLDR; Clone and run Deployment_wrapper.sh WITHOUT sudo privileges. At some point it will ask for it. Enter you password, continue. Wait. Voila'

## How to add software to this deployment implementation
* Python2 - Python 2 related libraries is installed to the Anaconda2 (base) env, which acts as the deafult python2 namespace. Use pip install or conda install. Programs (ex. MultiQC) are installed to their specific environments. Simply add commands to Deployment_wrapper.sh (Under Install conda packages and bundles)
* Python3 - Programs (ex. Unicycler) are installed the same way as with python2 if available in any conda-channel, however $PATH defaults to /usr/bin/python3 There is no conda base python3 env.
* Aptitude - Installed simply by adding the package name in the packages list in SfB-course-install.py
* Local scripts, documentation etc.  - Add to git repo.
* Everything else - Create a module using one of the existing templates in modules/ as a basis. The module will be wrapped by SfB-course-install.py automatically.

## Deployment_wrapper.sh
This script installs and sets up everything.
1. Downloads, installs and configures Anaconda2, which replaces the standard /usr/bin/python with (base) anaconda2 python
2. Sets up an Ubuntu launcher for using Jupyter-notebook for easy viewing of practicals and other documentation. Working directory defaults to $HOME/Practicals
3. Installs all necessary python2 dependencies to (base) env
4. Installs all bundles of programs available either as python 2 or 3 to their own specific environments
5. Installs libapt-pkg, needed for SfB-course-install.py to run
6. Installs all standalone modules using SfB-course-install.py

## SfB-course-install.py
This script will install all* necessary programs used in courses provided by SfB. Only works with Ubuntu (integrates with Aptitude)

(* with some obvious exceptions which require interactive promts/licenses)

All installable modules are described as python functions available in modules/ and can be run independently (single installation of one program) or wrapped by SfB-course-install.py (installs every module present in modules/)

Dependencies:

libapt-pkg (installed with sudo apt-get install python-apt on ubuntu systems)
