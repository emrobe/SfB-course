# Module: Ugene
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./ugene-1.29.0/ugene'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Ugene..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "ugene.unipro.ru/downloads/ugene-1.29.0-x86-64-full.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", '-zxvf', "ugene-1.29.0-x86-64-full.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "ugene-1.29.0-x86-64-full.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('ugene-1.29.0')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Ugene - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Ugene is already installed."
