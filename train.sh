#!/bin/bash
#LOG=/home/ying/Public/caffe/examples/zhj/ResNetFC/log/skip/train-`date +%Y-%m-%d-%H-%M-%S`.log
#CAFFE=/home/ying/Public/caffe/build/tools/caffe

#LOG=/home/zhaohj/Documents/Code/ResNetFC/log/skip_2/train-`date +%Y-%m-%d-%H-%M-%S`.log
LOG=/home/zhaohj/Documents/Code/FCN-ResNet50/log/3_lr.log
CAFFE=/home/zhaohj/caffe/build/tools/caffe

#$CAFFE train --solver=solver_res50_skip.prototxt --weights /home/ying/Public/caffe/examples/zhj/ResNet/ResNet-50-model.caffemodel 2>&1 | tee $LOG
#$CAFFE train --solver=solver.prototxt --weights /home/zhaohj/github/ResNet/ResNet-50-model.caffemodel 2>&1 | tee $LOG

#$CAFFE train --solver=solver.prototxt --weights ./snapshot/train_iter_300000.caffemodel 2>&1 | tee $LOG
$CAFFE train --solver=solver.prototxt -snapshot ./snapshot/train_iter_270000.solverstate 2>&1 | tee $LOG
#$CAFFE train --solver=solver_res50.prototxt  2>&1 | tee $LOG

