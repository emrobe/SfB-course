# Module: KAT
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./kat-2.3.4/configure'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling KAT..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["wget", "https://github.com/TGAC/KAT/releases/download/Release-2.3.4/kat-2.3.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tExtracting..."
			subprocess.call(["tar", "-zxvf", "kat-2.3.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			os.chdir('kat-2.3.4')
			print "\t\tCompiling..."
			subprocess.call(["bash", "configure"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["make"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["make", "install"], stdout=FNULL, stderr=FNULL)
			os.chdir('..')
			subprocess.call(["rm", "kat-2.3.4.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: KAT - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "KAT is already installed."
