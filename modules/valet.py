# Module: VALET
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./VALET/src/py/pipeline.py'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling VALET..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/jgluck/VALET.git"], stdout=FNULL, stderr=FNULL)
			print "\t\tBuilding..."
			os.chdir('VALET')
			subprocess.call(["bash", "setup.sh"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('src/py')
			path = os.getcwd()
			os.chdir('../../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: VALET - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "VALET is already installed."
