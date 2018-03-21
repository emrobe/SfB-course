# Module: Blobtools
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./blobtools'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Blobtools..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/DRL/blobtools.git"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnpacking..."
			os.chdir('blobtools')
			print "\t\tCompiling..."
			subprocess.call(["./install"], stdout=FNULL, stderr=FNULL)
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, pip
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Blobtools - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Blobtools is already installed."