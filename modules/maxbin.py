# Module: Maxbin
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./MaxBin-2.2.4/src/MaxBin'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Maxbin..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			subprocess.call(["wget", "https://downloads.sourceforge.net/project/maxbin/MaxBin-2.2.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "MaxBin-2.2.4.tar.gz"], stdout=FNULL, stderr=FNULL)
			os.chdir('MaxBin-2.2.4/src')
			subprocess.call(["make"], stdout=FNULL, stderr=FNULL)
			os.chdir('..')
			path = os.getcwd()
			# Configure deps manually:
			with open("setting", "w") as handle:
				os.chdir('..')
				fgs = '[FragGeneScan] '
				fgs += os.path.join(os.getcwd(), 'FragGeneScan1.30')
				b2 = '[Bowtie2] '
				b2 += '/usr/bin'
				hmm = '[HMMER3] '
				hmm += os.path.join(os.getcwd(), 'hmmer-3.1b2-linux-intel-x86_64/binaries')
				idba = '[IDBA_UD] '
				idba += os.path.join(os.getcwd(), 'idba/bin')
				handle.write(fgs+"\n")
				handle.write(b2+"\n")
				handle.write(hmm+"\n")
				handle.write(idba+"\n")

			subprocess.call(["rm", "MaxBin-2.2.4.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Maxbin - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Maxbin is already installed."
