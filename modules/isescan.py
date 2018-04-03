# Module: Isescan
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./ISEScan-1.5.4.3/isescan.py'):
				return True
			else:
				return False
		except Exception as e:
			return e
	if action == 'install':
		try:
			print "\tInstalling ISEScan..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://github.com/xiezhq/ISEScan/archive/v1.5.4.3.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["tar", "-zxvf", "v1.5.4.3.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "v1.5.4.3.tar.gz"], stdout=FNULL, stderr=FNULL)
			os.chdir('ISEScan-1.5.4.3')
			path = os.getcwd()
			print "\t\tCompiling..."
			os.chdir('ssw201507')
			subprocess.call(["cc", "-Wall", "-O3", "-pipe", "-fPIC", "-shared", "-rdynamic", "-o", "libssw.so", "ssw.c", "ssw.h"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["cp", "sswlib.so", '../.'], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
				source.write('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:libssw.so'+"\n")
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Isescan - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Isescan is already installed."
