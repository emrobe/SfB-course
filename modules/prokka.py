# Module: Prokka
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./prokka'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Prokka..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/tseemann/prokka.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('prokka/bin')
			print "\t\tCompiling..."
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, cpan, libdatetime-perl, libxml-simple-perl, libdigest-md5-perl, default-jre, bioperl
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Prokka - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Prokka is already installed."
