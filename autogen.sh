#!/bin/bash
# Michael Scales
# Also need to add /usr/local/bin > /etc/ld.so.conf
# http://jrmeyer.github.io/asr/2016/01/09/Installing-CMU-Sphinx-on-Ubuntu.html

cd .. # Move outside the project directory
git clone https://github.com/cmusphinx/sphinxbase.git
cd sphinxbase
./autogen.sh
make
make install
cd ..

git clone https://github.com/cmusphinx/pocketsphinx.git
cd pocketsphinx
./autogen.sh
make
make install
cd ..
exit 0
