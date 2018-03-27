# Module: Fasttree
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./Fasttree/'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling FastQC..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["mkdir", "Fasttree"], stdout=FNULL, stderr=FNULL)
			os.chdir('Fasttree')
			path = os.getcwd()
			subprocess.call(["wget", "http://microbesonline.org/fasttree/FastTreeDbl"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["chmod", "a+x","FastTreeDbl"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Fasttree - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Fasttree is already installed."
