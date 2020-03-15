#!/bin/sh

set -e

DIR=`pwd`
LOG=$DIR/jasper-installer.log

# Download and extract packages for STT
# The Pocketsphinx STT engine requires the MIT Language Modeling Toolkit,
# m2m-aligner, Phonetisaurus and OpenFST
wget http://downloads.sourceforge.net/project/cmusphinx/sphinxbase/0.8/sphinxbase-0.8.tar.gz
wget http://downloads.sourceforge.net/project/cmusphinx/pocketsphinx/0.8/pocketsphinx-0.8.tar.gz
wget http://distfiles.macports.org/openfst/openfst-1.3.4.tar.gz
wget https://github.com/mitlm/mitlm/releases/download/v0.4.1/mitlm_0.4.1.tar.gz
wget https://m2m-aligner.googlecode.com/files/m2m-aligner-1.2.tar.gz
wget https://phonetisaurus.googlecode.com/files/is2013-conversion.tgz
wget https://www.dropbox.com/s/kfht75czdwucni1/g014b2b.tgz
svn co https://svn.code.sf.net/p/cmusphinx/code/trunk/cmuclmtk/
tar xvf sphinxbase-0.8.tar.gz
tar xvf pocketsphinx-0.8.tar.gz
tar xvf m2m-aligner-1.2.tar.gz
tar xvf openfst-1.3.4.tar.gz
tar xvf is2013-conversion.tgz
tar xvf mitlm_0.4.1.tar.gz
tar xvf g014b2b.tgz

# Install Speech-To-Text Engine Pocketsphinx and CMUCLMTK
echo "$(date) - Building sphinxbase-0.8..." >> $LOG
cd $DIR/sphinxbase-0.8/
./configure --enable-fixed
make -j2
sudo make install
echo "$(date) - Completed building and installing sphinxbase-0.8..." >> $LOG

echo "$(date) - Building pocketshinx-0.8..." >> $LOG
cd $DIR/pocketsphinx-0.8/
./configure
make -j2
sudo make install
echo "$(date) - Completed building and installing pocketshinx-0.8..." >> $LOG

echo "$(date) - Building cmuclmtk..." >> $LOG
cd $DIR/cmuclmtk/
sudo ./autogen.sh
sudo make -j2
sudo make install
echo "$(date) - Completed building and installing cmuclmtk..." >> $LOG

# Install OpenFST
echo "$(date) - Building openfst-1.3.4..." >> $LOG
cd $DIR/openfst-1.3.4/
./configure --enable-compact-fsts --enable-const-fsts --enable-far --enable-lookahead-fsts --enable-pdt
make
sudo make install
echo "$(date) - Completed building and installing openfst-1.3.4..." >> $LOG

# Install M2M, MITLMT, Phonetisaurus and Phonetisaurus FST
echo "$(date) - Building m2m-aligner-1.2..." >> $LOG
cd $DIR/m2m-aligner-1.2/
make -j2
sudo cp $DIR/m2m-aligner-1.2/m2m-aligner /usr/local/bin/m2m-aligner
echo "$(date) - Completed building and installing m2m-aligner-1.2..." >> $LOG

echo "$(date) - Building mitlm_0.4.1..." >> $LOG
cd $DIR/mitlm_0.4.1/
./configure
make -j2
sudo make install
echo "$(date) - Completed building and installing mitlm_0.4.1..." >> $LOG

echo "$(date) - Building is2013-conversion..." >> $LOG
cd $DIR/is2013-conversion/phonetisaurus/src/
make -j2
sudo cp $DIR/is2013-conversion/bin/phonetisaurus-g2p /usr/local/bin/phonetisaurus-g2p
echo "$(date) - Completed building and installing is2013-conversion..." >> $LOG

echo "$(date) - Building g014b2b..." >> $LOG
echo "$(date) - Export the LD_LIBRARY_PATH for fstcompiler..." >> $LOG
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib
ldconfig  # As in https://github.com/nexhero/Easy-Jasper/issues/1

cd $DIR/g014b2b/
./compile-fst.sh
cd
mv $DIR/g014b2b $DIR/phonetisaurus
echo "$(date) - Completed building and installing g014b2b..." >> $LOG