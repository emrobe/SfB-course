# Module: Metaprob
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./MetaProb/Release/MetaProb'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Metaprob..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://bitbucket.org/samu661/metaprob/downloads/MetaProb_v2.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "MetaProb_v2.tar.gz"], stdout=FNULL, stderr=FNULL)
			os.chdir('MetaProb/Release')
			subprocess.call(["make", "all"], stdout=FNULL, stderr=FNULL)
			path = os.getcwd()
			os.chdir('../..')
			subprocess.call(["rm", "MetaProb_v2.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Metaprob - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Metaprob is already installed."
