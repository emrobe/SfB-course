# Module: BBMap
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./bbmap/bbmap.sh'):
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
			subprocess.call(["wget", "https://downloads.sourceforge.net/project/bbmap/BBMap_37.78.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "BBMap_37.78.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "BBMap_37.78.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('bbmap')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: BBMap - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "BBMap is already installed."
