# Module: Bandage
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./bandage'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Bandage..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["mkdir", "bandage"], stdout=FNULL, stderr=FNULL)
			os.chdir('bandage')
			subprocess.call(["wget", "https://github.com/rrwick/Bandage/releases/download/v0.8.1/Bandage_Ubuntu_dynamic_v0_8_1.zip"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["unzip", "Bandage_Ubuntu_dynamic_v0_8_1.zip"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "Bandage_Ubuntu_dynamic_v0_8_1.zip"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tCompiling..."
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: wget, unzip
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Bandage - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Bandage is already installed."
