# Scripts to run SU2 with spython and Singularity


## Install requirements

Install Singularity
~~~~
VERSION=3.0.0
wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
tar xvf singularity-$VERSION.tar.gz
cd singularity-$VERSION
./configure --prefix=/usr/local
make
sudo make install
~~~~

Install Spython for python3
~~~~
sudo apt-get python3 python3-pip
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install spython
~~~~

## Run the testcase
~~~~
python3 run_su2.py
~~~~


