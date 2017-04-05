import caffe
import surgery, score

import numpy as np
import os
import sys

try:
    import setproctitle
    setproctitle.setproctitle(os.path.basename(os.getcwd()))
except:
    pass

weights = '/home/zhaohj/github/ResNet/ResNet-50-model.caffemodel'
#weights = './snapshot//train_iter_2000.solverstate'

# init
caffe.set_device(0)
caffe.set_mode_gpu()

solver = caffe.SGDSolver('./solver.prototxt')
solver.net.copy_from(weights)

# scoring
val = np.loadtxt('./data/pascal/seg11valid.txt', dtype=str)

for _ in range(25):
    solver.step(4000)
    score.seg_tests(solver, False, val, layer='score')
