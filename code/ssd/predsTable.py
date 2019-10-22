import time
from matplotlib import pyplot as plt
import numpy as np
import mxnet as mx
from mxnet import autograd, gluon
import gluoncv as gcv
from gluoncv.utils import download, viz
import cv2

classes = ['table']
net = gcv.model_zoo.get_model('ssd_512_resnet50_v1_custom', classes=classes, pretrained_base=False)
net.load_parameters('ssd_512_resnet50_tablebank_19.params')

def predict(imagePath):
    image = cv2.imread(imagePath)
    output = image.copy()
    (hI, wI, d) = image.shape
    x, image = gcv.data.transforms.presets.ssd.load_test(imagePath,min(wI,hI),max_size=max(wI,hI))
    cid, score, bbox = net(x)
    for (box, score) in zip(bbox[0], score[0]):
        if score < 0.5:
            continue
        cv2.rectangle(output, (box[0].asscalar(), box[1].asscalar()), (box[2].asscalar(), box[3].asscalar()),(0, 255, 0), 2)
    cv2.imwrite("prediction.jpg", output)




import matplotlib.pyplot as plt
def showImage(image):
    if len(image.shape)==3:
        img2 = image[:,:,::-1]
        plt.imshow(img2)
        plt.show()
    else:
        img2 = image
        plt.imshow(img2,cmap='gray')
        plt.show()
