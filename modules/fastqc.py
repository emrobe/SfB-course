# Module: FastQC
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./FastQC/fastqc'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling FastQC..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["unzip", "fastqc_v0.11.5.zip"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["chmod", "a+x","FastQC/fastqc"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "fastqc_v0.11.5.zip"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('FastQC')
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: FastQC - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "FastQC is already installed."
