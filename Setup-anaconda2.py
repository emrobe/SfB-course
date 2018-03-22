#!/usr/bin/python
import getpass, os, argparse, pkgutil, sys, subprocess

# Install Anaconda2
def install_conda(args):
        if args.install:
                if not os.path.isfile(os.path.join(os.path.expanduser("~"), 'anaconda2/bin/conda')):
                        print "\tInstalling Anaconda2..."
                        FNULL = open(os.devnull, 'w')
                        print "\t\tDownloading Anaconda2..."
                        subprocess.call(["wget", "https://repo.continuum.io/archive/Anaconda2-5.1.0-Linux-x86_64.sh", '-O', 'anaconda2.sh'], stdout=FNULL, stderr=FNULL)
                        print "\t\tSetting up Anaconda2..."
                        subprocess.call(['bash', 'anaconda2.sh', '-b', '-p', '$HOME/anaconda2'], stdout=FNULL, stderr=FNULL)
                        subprocess.call(['rm', 'anaconda2.sh'], stdout=FNULL, stderr=FNULL, close_fds=True)
                        if os.environ.has_key('SUDO_USER'):
                                user = os.environ['SUDO_USER']
                                install_path = os.path.join(os.path.expanduser("~"), 'anaconda2/')
                                set_permissions = 'chown -R '+user+':'+user+' '+install_path
                                subprocess.call(set_permissions, shell=True)
				print "\tExecuted with sudo, chowned to "+os.environ['SUDO_USER']
                        else:
                                print "\tExecuted without sudo, no permissions changed."
                else:
                        print "\tAnaconda2 already installed."
        if args.list:
                if os.path.isfile(os.path.join(os.path.expanduser("~"), 'anaconda2/bin/conda')):
                        print "\tAnaconda2 already installed"
                else:
                        print "\tAnaconda2 not installed."

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="This script downloads and installs Anaconda2, specificaly configured for the SfB-course-install.py deployment script. \nInstalls to $HOME/anaconda2, should not be run with superuser privileges)")
        parser.add_argument('--install', action='store_true', help='Installs, configures and sets Anaconda2 as default python 2.7 interpreter. (Performs a check first)')
        parser.add_argument('--list', action='store_true', help='Checks for an existing SfB-configured Anaconda2 installation.')

        args = parser.parse_args()

        if not args.install and not args.list:
                exit('Please run with --install to install and configure Anaconda2, or --list to check installation')

        # Install
        install_conda(args)

