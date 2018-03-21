# Module: AUGUSTUS
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./augustus'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling AUGUSTUS..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "http://augustus.gobics.de/binaries/augustus.2.5.5.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "zxvf", "augustus.2.5.5.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "augustus.2.5.5.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tCompiling..."
			os.chdir('augustus.2.5.5/bin')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: wget
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: AUGUSTUs - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "AUGUSTUS is already installed."