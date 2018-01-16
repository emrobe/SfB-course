# Module: MapSeq
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./mapseq-1.2.2-linux/mapseq'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Mapseq..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "http://meringlab.org/software/mapseq/mapseq-1.2.2-linux.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "mapseq-1.2.2-linux.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "mapseq-1.2.2-linux.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('mapseq-1.2.2-linux')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Mapseq - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Mapseq is already installed."
