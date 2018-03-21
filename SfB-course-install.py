#!/usr/bin/python
import getpass, os, argparse, pkgutil, sys, subprocess

# Install or list modules available from apt. (Ubuntu only)
def apt_specific_modules(args):
	import apt

	packages = ['curl','gnuplot','python3-matplotlib','libtool','cython','python-setuptools','build-essential','libgsl-dev','r-base-core','openjfx','python-matplotlib','autoconf', 'automake', 'libeigen3-dev', 'libboost-all-dev', 'zlib1g-dev','git','bowtie2', 'ncbi-blast+', 'samtools', 'python-htseq', 'default-jre', 'python-biopython', 'abacas', 'libdatetime-perl', 'libxml-simple-perl', 'libdigest-md5-perl', 'bioperl', 'cmake', 'qtbase5-dev', 'libqt5svg5-dev', 'qt5-default', 'tabix', 'python-pip']
	packages = sorted(packages)
	
	cache = apt.cache.Cache()
	cache.update()

	print "APT status:"

	for module in packages:
		module = cache[module]
		if args.list:
			if module.is_installed:
				print "\t{0} already installed, version: {1}".format(module.name, module.versions)
			else:
				print "\t{0} is not installed".format(module.name)
		elif args.install:
			if not module.is_installed:
				print "\t{0} marked for installation".format(module.name)
				module.mark_install()
			else:
				print "\t{0} already installed, version: {1}".format(module.name, module.versions)
	
	if args.install:
		print "Installing marked packages..."
		cache.commit()


# Iterate over all modules available in modules. Run check or check-install
def load_all_modules_from_dir(dirname):
	for importer, package_name, _ in pkgutil.iter_modules([dirname]):
		full_package_name = '%s.%s' % (dirname, package_name)
		if full_package_name not in sys.modules:
			module = importer.find_module(package_name).load_module(full_package_name)
		
		if args.install and module.commence('check') != True:
			print "\nChecking... "+module.__name__
			print "\tNot found in "+str(os.getcwd())
			module.commence('install')

		else:
			print "\nChecking... "+module.__name__
			print "\tAlready installed."

def list_all_modules(dirname):
	print "\nSfB modules staged for deployment:"
	for importer, package_name, _ in pkgutil.iter_modules([dirname]):
		full_package_name = '%s.%s' % (dirname, package_name)
		print "\t{0}".format(full_package_name)

if __name__ == '__main__':
	# Yeah, i know right...
	import warnings
	warnings.filterwarnings("ignore")

	parser = argparse.ArgumentParser(description='This script will install all programs and dependencies needed in SfB metagenomic courses. Run with sudo priviledges. Any programs or dependencies already installed will be skipped. Needs the python-apt library (install with apt-get install python-apt)')
	parser.add_argument('--install', action='store_true', help='Installs all available modules. (Performs a check first)')
	parser.add_argument('--list', action='store_true', help='List all programs and dependencies staged for deployment.')
	
	args = parser.parse_args()
	
	if not args.install and not args.list:
	        exit('Please run with --install to install all modules or --list to see modules staged for deployment')

	apt_specific_modules(args)

	if args.install:
		load_all_modules_from_dir('modules')
	if args.list:
		list_all_modules('modules')

	# Chown all installed programs to current user	
	if os.environ.has_key('SUDO_USER'):
		user = os.environ['SUDO_USER']
		set_permissions = 'chown -R '+user+':'+user+' *'
		subprocess.call(set_permissions, shell=True)
	else:
		print "Executed without sudo, no permissions set."
