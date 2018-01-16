# Module: SeqKit
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			if os.path.isfile('./seqkit/seqkit'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling SeqKit..."
			FNULL = open(os.devnull, 'w')
			print "\t\tDownloading..."
			os.mkdir('seqkit')
			os.chdir('seqkit')
			subprocess.call(["wget", "https://github.com/shenwei356/seqkit/releases/download/v0.7.2/seqkit_linux_amd64.tar.gz"], stdout=FNULL, stderr=FNULL)
			print "\t\tUnziping..."
			subprocess.call(["tar", "-zxvf", "seqkit_linux_amd64.tar.gz"], stdout=FNULL, stderr=FNULL)
			subprocess.call(["rm", "seqkit_linux_amd64.tar.gz"], stdout=FNULL, stderr=FNULL, close_fds=True)
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: SeqKit - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "SeqKit is already installed."
