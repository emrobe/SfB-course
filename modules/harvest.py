# Module: HarvestTools
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./Harvest-Linux64-v1.1.2/harvesttools'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Harvest..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://github.com/marbl/harvest/releases/download/v1.1.2/Harvest-Linux64-v1.1.2.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "Harvest-Linux64-v1.1.2.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "Harvest-Linux64-v1.1.2.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('Harvest-Linux64-v1.1.2')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Harvest - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Harvest is already installed."
