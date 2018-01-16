# Module: Megahit
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
			FNULL = open(os.devnull, 'w')
			subprocess.check_call(['./megahit/megahit -v'], stdout=FNULL, stderr=FNULL, close_fds=True, shell=True)
			return True
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling Megahit..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/voutcn/megahit.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('megahit')
			print "\t\tCompiling..."
			subprocess.call(["make"], stdout=FNULL, stderr=FNULL, close_fds=True)
			path = os.getcwd()
			os.chdir('..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: Megahit - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "Megahit is already installed."
