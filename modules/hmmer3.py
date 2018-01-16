# Module: HMMer3
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./hmmer-3.1b2-linux-intel-x86_64/binaries/hmmscan'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling HMMer3..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "hmmer-3.1b2-linux-intel-x86_64.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "hmmer-3.1b2-linux-intel-x86_64.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('hmmer-3.1b2-linux-intel-x86_64/binaries')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: HMMer3 - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "HMMer3 is already installed."
