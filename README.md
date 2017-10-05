# pytorch-caffe2-aws-lambda

AWS Lambda Function with Numpy, protobuf, pillow, Caffe2 and ONNX

Can run Caffe2 models and PyTorch models converted with ONNX

Inspired by [LINK](https://github.com/cemoody/lambda-chainer)

Instructions:

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
    pip install onnx
    cd ~

    mkdir cf2

    git clone --recursive https://github.com/caffe2/caffe2.git && cd caffe2

    mkdir build && cd build

    cmake -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX="/home/ec2-user/cf2/" -DCMAKE_PREFIX_PATH="/home/ec2-user/cf2/" -DUSE_GFLAGS=OFF  ..
    make -j4
    make install/fast

    cd ~
    git clone --recursive https://github.com/onnx/onnx-caffe2
    cd onnx-caffe2
    git reset --hard f7509f293d781638ef14ac3d232de0c140ed8277
    python setup.py install

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

    cd cf2
    zip -9 -q -r ~/deps.zip caffe2
    cd ~

    mkdir local
    mkdir local/lib

    cp /usr/lib64/libprotobuf.so* local/lib/

    zip -9 -q -r ~/deps.zip local/lib
    zip -9 -q -r ~/deps.zip test.py
