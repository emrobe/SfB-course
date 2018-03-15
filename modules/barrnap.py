# Module: Barrnap
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./barrnap'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Barrnap..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/tseemann/barrnap.git"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnpacking..."
			os.chdir('barrnap/bin')
			print "\t\tCompiling..."
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, cpan, libdatetime-perl, libxml-simple-perl, libdigest-md5-perl, default-jre, bioperl
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Barrnap - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Barrnap is already installed."