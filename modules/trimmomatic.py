# Module: Trimmomatic
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./Trimmomatic-0.36/trimmomatic-0.36.jar'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Trimmomatic..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["unzip", "Trimmomatic-0.36.zip"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["chmod", "a+x","Trimmomatic-0.36/trimmomatic-0.36.jar"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "Trimmomatic-0.36.zip"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('Trimmomatic-0.36')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Trimmomatic - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Trimmomatic is already installed."
