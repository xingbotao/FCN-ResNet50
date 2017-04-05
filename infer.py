import numpy as np
from PIL import Image

import matplotlib.pyplot as plt

import caffe

# load image, switch to BGR, subtract mean, and make dims C x H x W for Caffe
#im = Image.open('/home/ying/Public/caffe/examples/zhj/ResNetFC/VOC2012/JPEGImages/2007_000129.jpg')
#im = Image.open('/home/zhaohj/github/FCN/data/pascal/VOC2012/JPEGImages/2007_000129.jpg')

im = Image.open('/home/zhaohj/Documents/Data/VOCdevkit/VOC2012_Augmentation/JPEGImages/2007_000129.jpg')
in_ = np.array(im, dtype=np.float32)
in_ = in_[:,:,::-1]
in_ -= np.array((104.00698793,116.66876762,122.67891434))
in_ = in_.transpose((2,0,1))

# load net
net = caffe.Net('deploy.prototxt', './snapshot/train_iter_310000.caffemodel', caffe.TEST)
# shape for input (data blob is N x C x H x W), set data
net.blobs['data'].reshape(1, *in_.shape)
net.blobs['data'].data[...] = in_
# run net and take argmax for prediction
net.forward()
out = net.blobs['score'].data[0].argmax(axis=0)
shape=net.blobs['score'].data.shape
w=net.params['fc6'][0].data
print w
print shape



#plt.imshow(out,cmap='gray');plt.axis('off')
plt.imshow(out);plt.axis('off')
plt.savefig('310000.png')
plt.show()

