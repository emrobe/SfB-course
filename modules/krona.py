# Module: KronaTools
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./Krona/KronaTools/scripts/ImportText.pl'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling KronaTools..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/marbl/Krona.git"], stdout=FNULL, stderr=FNULL)
			default_path = os.getcwd()
			os.chdir('Krona/KronaTools')
			print "\t\tInstalling..."
			path = os.getcwd()
			subprocess.call(["perl", "install.pl", "--prefix", path], stdout=FNULL, stderr=FNULL, close_fds=True)
			path = os.path.join(path, 'bin/')
			os.chdir(default_path)
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: KronaTools - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "KronaTools is already installed."
