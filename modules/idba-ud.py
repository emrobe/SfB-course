# Module: IDBA-UD
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./idba/bin/idba'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling IDBA-UD..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/loneknightpy/idba.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('idba')
			print "\t\tCompiling..."
			subprocess.call(["bash", "build.sh"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('bin')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: IDBA - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "IDBA is already installed."
