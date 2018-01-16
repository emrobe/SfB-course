# Module: IGV
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./IGV_2.4.6/igv.sh'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling IGV..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "http://data.broadinstitute.org/igv/projects/downloads/2.4/IGV_2.4.6.zip"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["unzip", "IGV_2.4.6.zip"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "IGV_2.4.6.zip"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('IGV_2.4.6')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: IGV - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "IGV is already installed."
