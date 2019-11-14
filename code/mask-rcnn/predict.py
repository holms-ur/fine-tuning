from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mrcnn import utils
import mrcnn.model as modellib
import skimage.io
import cv2
 
class TestConfig(Config):
     NAME = "test"
     GPU_COUNT = 1
     BACKBONE = "resnet50"
     IMAGE_RESIZE_MODE = "square"
     IMAGE_MIN_DIM = 512
     IMAGE_MAX_DIM = 512
     IMAGES_PER_GPU = 1
     NUM_CLASSES = 1 + 1
 
# define the model
rcnn = MaskRCNN(mode='inference', model_dir='./', config=TestConfig())
# load coco model weights
# J. modificar con el path al modelo. 
rcnn.load_weights('mask_rcnn_tablebank_cfg_0002.h5', by_name=True)
# load photograph

def predict(imagePath):
    img = load_img(imagePath)
    img = img_to_array(img)
    output = img.copy()
    # make prediction
    results = rcnn.detect([img], verbose=0)
    r = results[0]
    for (box, score) in zip(r['rois'], r['scores']):
          # filter out weak detections
          if score < 0.5:
               continue
          label = "{}: {:.2f}".format('table', score)
          cv2.rectangle(output, (box[1], box[0]), (box[3], box[2]),(0, 255, 0), 2)
          cv2.putText(output, label, (box[1], box[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imwrite("prediction.jpg", output)
    return r['rois']




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
