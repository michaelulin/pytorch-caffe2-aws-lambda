# pytorch-caffe2-aws-lambda

sudo yum update -y
sudo yum -y upgrade
sudo yum -y groupinstall "Development Tools"

sudo yum install -y \
automake \
cmake \
protobuf-devel \
python-devel \
python-pip \
git

sudo yum install -y gcc zlib zlib-devel openssl openssl-devel
sudo yum install -y libjpeg-devel

pip install virtualenv
virtualenv ~/env && cd ~/env && source bin/activate
pip install numpy

pip install --use-wheel --no-index -f http://dist.plone.org/thirdparty/ -U PIL --trusted-host dist.plone.org
pip install protobuf
pip install future
pip install requests
cd
touch env/lib/python2.7/site-packages/google/__init__.py

mkdir cf3

git clone --recursive https://github.com/caffe2/caffe2.git && cd caffe2

mkdir build && cd build

cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX="/home/ec2-user/cf3/" -DCMAKE_PREFIX_PATH="/home/ec2-user/cf3/" -DUSE_GFLAGS=OFF  ..
make -j20
make install/fast

cd ~
for dir in $VIRTUAL_ENV/lib64/python2.7/site-packages \
	   $VIRTUAL_ENV/lib/python2.7/site-packages
do
  if [ -d $dir ] ; then
    pushd $dir; zip -9 -q -r ~/deps.zip .; popd
  fi
done

git clone https://github.com/google/protobuf.git
cd protobuf
zip -9 -q -r ~/deps.zip python

cd ~

cd cf3
zip -9 -q -r ~/deps.zip caffe2
cd ~

mkdir local
mkdir local/lib

cp /usr/lib64/libprotobuf.so* local/lib/

zip -r ~/deps.zip local/lib

zip -9 -q -r ~/deps.zip helper.py

zip -9 -q -r ~/deps.zip lambda.py
