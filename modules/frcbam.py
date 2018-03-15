# Module: FRCbam
def commence(action):
	import subprocess, os
	if action == 'check':
		try:
                        if os.path.isfile('./FRC_align/bin/frcbam'):
				return True
			else:
				return False
		except Exception as e:
			return e

	if action == 'install':
		try:
			print "\tInstalling FRCbam..."
			FNULL = open(os.devnull, 'w')
			print "\t\tCloning from git..."
			subprocess.call(["git", "clone", "https://github.com/vezzi/FRC_align.git"], stdout=FNULL, stderr=FNULL)
			os.chdir('FRC_align')
			print "\t\tCompiling..."
			subprocess.call(["mkdir", "build"], stdout=FNULL, stderr=FNULL)
			os.chdir('build')
			subprocess.call(["cmake", ".."], stdout=FNULL, stderr=FNULL, close_fds=True)
			subprocess.call(["make"], stdout=FNULL, stderr=FNULL, close_fds=True)
			os.chdir('../bin')
			path = os.getcwd()
			os.chdir('../..')
			print "\t\tWriting paths to PATH_additions.txt..."
			with open("SfB_path_additions.txt", "a") as source:
				source.write('export PATH='+path+':$PATH'+"\n")
			# deps: git, qmake, make(gcc)
			print "\t\tSuccess."
		except Exception as e:
			print "WARNING: FRCbam - This deployment module needs an update or dependenciess are not met. Caught exception: "+str(e)

if __name__ == '__main__':
	# Check if installed (exists in PATH) 
	installed = commence('check')
	#print installed
	# Install
	if installed != True:
		pass
		commence('install')
	else:
		print "FRCbam is already installed."
