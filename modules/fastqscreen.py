# Module: FastQ Screen
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./fastq_screen_v0.11.4/fastq_screen'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling FastQ Screen..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://www.bioinformatics.babraham.ac.uk/projects/fastq_screen/fastq_screen_v0.11.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tExtracting..."
			subprocess.call(["tar", "-zxvf", "fastq_screen_v0.11.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			#subprocess.call(["chmod", "a+x","FastQC/fastqc"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "fastq_screen_v0.11.4.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('fastq_screen_v0.11.4')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: FastQ Screen - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "FastQ Screen is already installed."
