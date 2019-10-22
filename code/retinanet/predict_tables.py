# USAGE
# python predict.py --model output.h5 --labels logos/retinanet_classes.csv \
# 	--image logos/images/786414.jpg --confidence 0.5

# import the necessary packages
from keras_retinanet.utils.image import preprocess_image
from keras_retinanet.utils.image import read_image_bgr
from keras_retinanet.utils.image import resize_image
from keras_retinanet import models
import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt



# load the class label mappings
LABELS = open("retinanet_classes.csv").read().strip().split("\n")
LABELS = {int(L.split(",")[1]): L.split(",")[0] for L in LABELS}

# load the model from disk
model = models.load_model("output.h5", backbone_name="resnet50")

def predict(imagePath):
	# load the input image (in BGR order), clone it, and preprocess it
	image = read_image_bgr(imagePath)
	output = image.copy()
	image = preprocess_image(image)
	(image, scale) = resize_image(image)
	image = np.expand_dims(image, axis=0)

	# detect objects in the input image and correct for the image scale
	(boxes, scores, labels) = model.predict_on_batch(image)
	boxes /= scale

	# loop over the detections
	for (box, score, label) in zip(boxes[0], scores[0], labels[0]):
		# filter out weak detections
		if score < 0.5:
			continue
	
		# convert the bounding box coordinates from floats to integers
		box = box.astype("int")
	
		# build the label and draw the label + bounding box on the output
		# image
		label = "{}: {:.2f}".format(LABELS[label], score)
		cv2.rectangle(output, (box[0], box[1]), (box[2], box[3]),
			(0, 255, 0), 2)
		cv2.putText(output, label, (box[0], box[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# show the output image
	cv2.imwrite("prediction.jpg", output)


def showImage(image):
    if len(image.shape)==3:
        img2 = image[:,:,::-1]
        plt.imshow(img2)
        plt.show()
    else:
        img2 = image
        plt.imshow(img2,cmap='gray')
        plt.show()

