# Module: RAxML
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./standard-RAxML/raxmlHPC-PTHREADS'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling RAxML..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/stamatak/standard-RAxML.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('standard-RAxML')
			path = os.getcwd()
			print "\t\tCompiling..."
			subprocess.call(["make", "-f", "Makefile.PTHREADS.gcc"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "*.o"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: RAxML - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "RAxML is already installed."
