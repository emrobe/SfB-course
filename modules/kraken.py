# Module: Kraken
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./kraken/kraken'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Kraken..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://ccb.jhu.edu/software/kraken/dl/kraken-1.0.tgz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "kraken-1.0.tgz"], stdout=FNULL, stderr=FNULL)
			os.chdir('kraken-1.0')
			print "\t\tCompiling..."
			subprocess.call(["bash", "install_kraken.sh", "../kraken"], stdout=FNULL, stderr=FNULL)
			os.chdir('../kraken')
			print "\t\tDownloading Minikraken DB files..."
			subprocess.call(["wget", "https://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["tar", "-zxvf", "minikraken_20171019_4GB.tgz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "minikraken_20171019_4GB.tgz"], stdout=FNULL, stderr=FNULL)
			path = os.getcwd()
			os.chdir('..')
			subprocess.call(["rm", "-rf","kraken-1.0"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "kraken-1.0.tgz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Kraken - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Kraken is already installed."
