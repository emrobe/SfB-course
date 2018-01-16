# Module: Desman
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./DESMAN/bin/desman'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Desman..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/chrisquince/DESMAN.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('DESMAN')
			print "\t\tCompiling..."
			subprocess.call(["python", "setup.py", "install"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('bin')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Desman - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Desman is already installed."
