# Module: Samtools
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./samtools'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Samtools..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 -O samtools.tar.bz2"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "xjvf", "samtools.tar.bz2"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "samtools.tar.bz2"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tCompiling..."
			os.chdir('samtools-1.3.1')
			subprocess.call(["make"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["make", "install"], stdout=FNULL, stderr=FNULL)
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: wget, gcc
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Samtools - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Samtools is already installed."