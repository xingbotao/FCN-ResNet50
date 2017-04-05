#!/bin/bash
LOG=2_lr.log
#CAFFE=/home/ying/Public/caffe
CAFFE=/home/zhaohj/caffe
sh parse_log.sh $LOG
$CAFFE/tools/extra/plot_training_log.py.example 6 2_lr.png $LOG
#    0: Test accuracy  vs. Iters 
#    1: Test accuracy  vs. Seconds 
#    2: Test loss  vs. Iters 
#    3: Test loss  vs. Seconds 
#    4: Train learning rate  vs. Iters 
#    5: Train learning rate  vs. Seconds 
#    6: Train loss  vs. Iters 
#    7: Train loss  vs. Seconds 
