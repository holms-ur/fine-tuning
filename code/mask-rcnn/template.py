from os import listdir
from xml.etree import ElementTree
from numpy import zeros
from numpy import asarray
from mrcnn.utils import Dataset
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
 
# class that defines and loads the tablebank dataset
class TableBankDataset(Dataset):
	# load the dataset definitions
	def load_dataset(self, dataset_dir, is_train=True):
		# define one class
		self.add_class("dataset", 1, "table")
		# define data locations
		images_dir = dataset_dir + '/images/'
		annotations_dir = dataset_dir + '/annots/'
		# find all images
		for filename in listdir(images_dir):
			# extract image id
			image_id = filename[:-4]
			# skip bad images
			#if image_id in ['00090']:
			#	continue
			# skip all images after 150 if we are building the train set
			#if is_train and int(image_id) >= 150:
			#	continue
			# skip all images before 150 if we are building the test/val set
			#if not is_train and int(image_id) < 150:
			#	continue
			img_path = images_dir + filename
			ann_path = annotations_dir + image_id + '.xml'
			# add to dataset
			self.add_image('dataset', image_id=image_id, path=img_path, annotation=ann_path)
 
	# extract bounding boxes from an annotation file
	def extract_boxes(self, filename):
		# load and parse the file
		tree = ElementTree.parse(filename)
		# get the root of the document
		root = tree.getroot()
		# extract each bounding box
		boxes = list()
		for box in root.findall('.//bndbox'):
			xmin = int(box.find('xmin').text)
			ymin = int(box.find('ymin').text)
			xmax = int(box.find('xmax').text)
			ymax = int(box.find('ymax').text)
			coors = [xmin, ymin, xmax, ymax]
			boxes.append(coors)
		# extract image dimensions
		width = int(root.find('.//size/width').text)
		height = int(root.find('.//size/height').text)
		return boxes, width, height
 
	# load the masks for an image
	def load_mask(self, image_id):
		# get details of image
		info = self.image_info[image_id]
		# define box file location
		path = info['annotation']
		# load XML
		boxes, w, h = self.extract_boxes(path)
		# create one array for all masks, each on a different channel
		masks = zeros([h, w, len(boxes)], dtype='uint8')
		# create masks
		class_ids = list()
		for i in range(len(boxes)):
			box = boxes[i]
			row_s, row_e = box[1], box[3]
			col_s, col_e = box[0], box[2]
			masks[row_s:row_e, col_s:col_e, i] = 1
			class_ids.append(self.class_names.index('table'))
		return masks, asarray(class_ids, dtype='int32')
 
	# load an image reference
	def image_reference(self, image_id):
		info = self.image_info[image_id]
		return info['path']
 
# define a configuration for the model
class TableBankConfig(Config):
	# define the name of the configuration
	NAME = "model_cfg"
	BACKBONE = "resnet50"
	IMAGE_RESIZE_MODE = "square"
	IMAGE_MIN_DIM = 512
	IMAGE_MAX_DIM = 512
	# number of classes (background + kangaroo)
	NUM_CLASSES = 1 + 1
	GPU_COUNT = 1
	IMAGES_PER_GPU = 4
	# number of training steps per epoch
	# <- MODIFY -> Replace 178 with the number of images of your dataset
	STEPS_PER_EPOCH = 178 // (GPU_COUNT * IMAGES_PER_GPU)
 
# prepare train set
train_set = TableBankDataset()
# <- MODIFY -> Replace mydataset with the name of the folder containing your images and annotations
train_set.load_dataset('mydataset', is_train=True)
train_set.prepare()
print('Train: %d' % len(train_set.image_ids))
# prepare config
config = TableBankConfig()
config.display()
# define the model
model = MaskRCNN(mode='training', model_dir='./', config=config)
# load weights (mscoco) and exclude the output layers
model.load_weights('mask_rcnn_tablebank_cfg_0002.h5', by_name=True, exclude=["mrcnn_class_logits", "mrcnn_bbox_fc",  "mrcnn_bbox", "mrcnn_mask"])
# train weights (output layers or 'heads')
model.train(train_set, None, learning_rate=config.LEARNING_RATE, epochs=2, layers='heads')
# unfreeze the body of the network and train *all* layers
model.train(train_set, None, epochs=5,layers="all", learning_rate=config.LEARNING_RATE / 10)

