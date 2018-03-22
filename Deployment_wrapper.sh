#!/bin/bash

echo "Deploying SfB-course..."

# Setup and configure anaconda2 for SfB-course
python Setup-anaconda2.py

# Setup jupyter notebook (launcher, icon, install-desktop, update-desktop-databases...etc)
echo "Icon=$HOME/SfB-course/mmp_logo.png" >> sfb.desktop
echo "Exec=$HOME/SfB-course/scripts/start_sfb_jupyter.sh" >> sfb.desktop
cp sfb.desktop $HOME/.local/share/applications

# Write to anaconda path .bashrc (Changes default python distribution to anaconda python)
echo "" >> $HOME/.bashrc
echo 'export PATH="$HOME/anaconda2/bin:$PATH"' >> $HOME/.bashrc

# Source .bashrc to set anaconda-specific python bins
source $HOME/.bashrc

# Setup conda envs, channels and install packages needed in default env (needed by SfB-course-install.py)
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

# Install Conda packages and bundles

### Packages (installs to default env (base))
conda install -y cython matplotlib htseq biopython

### Bundles (installs to their own environment, with specific options such as python versions)
conda create -y -n Busco python=3
conda install -y --name Busco busco
conda create -y -n Shovill
conda install -y --name Shovill shovill
conda create -y -n Abricate
conda install -y --name Abricate abricate
conda create -y -n Unicycler python=3
conda install -y --name Unicycler unicycler

# Run course install script, needs sudo and libapt-pkg installed
sudo apt-get install python-apt
sudo python SfB-course-install.py --install

# Write to .bashrc (SfB_path_additions.txt)
DIR=`pwd`
echo 'source $DIR/SfB_path_additions.txt' >> $HOME/.bashrc

# Source .bashrc to include 
source $HOME/.bashrc

# Update desktop database to view application in launcher
sudo update-desktop-database
