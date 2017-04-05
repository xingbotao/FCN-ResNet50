import caffe
import score

import numpy as np
import os
import sys

try:
    import setproctitle
    setproctitle.setproctitle(os.path.basename(os.getcwd()))
except:
    pass

weights = './snapshot/train_iter_300000.caffemodel'

# init
caffe.set_device(0)
caffe.set_mode_gpu()

solver = caffe.SGDSolver('./solver.prototxt')
solver.net.copy_from(weights)

# scoring
val = np.loadtxt('/home/zhaohj/Documents/Data/VOCdevkit/VOC2012_Augmentation/ImageSets/Segmentation/val.txt', dtype=str)

score.seg_tests(solver, False, val, layer='score')
