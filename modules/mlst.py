# Module: MLST
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./mlst/bin/mlst'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling MLST..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/tseemann/mlst.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('mlst/bin')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: MLST - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "MLST is already installed."
