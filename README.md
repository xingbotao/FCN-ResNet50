# FCN-ResNet50
This is a Fully Convolutional Networks(FCN), which is based on ResNet50, for Semantic Segmentation. I have fine tuned this net with VOC2012 train set, horizontal flip for data augmentation.

I tried to change the filter size in fc6 from 1\*1 to 7\*7 with padding 3. But there was no improvement.
I guess the reason is that I reduced the number of filters in fc6 and fc7.

## Download Model

fc6 layer with size 1\*1: [Google Drive](https://drive.google.com/open?id=0BwOAQMGvXhp2UWZVY0w4OE52SlU)

fc6 layer with size 7\*7: [Google Drive](https://drive.google.com/open?id=0BwOAQMGvXhp2TV9XYnBneEdnZms)
