# Module: FragGeneScan
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./FragGeneScan1.30/FragGeneScan'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling FragGeneScan..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://downloads.sourceforge.net/project/fraggenescan/FragGeneScan1.30.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "FragGeneScan1.30.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "FragGeneScan1.30.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('FragGeneScan1.30')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: FragGeneScan - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "FragGeneScan is already installed."
