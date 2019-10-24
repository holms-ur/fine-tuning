# Fine tuning with the Mask RCNN algorithm.

## Installation 

Install the [RetinaNet library](https://github.com/fizyr/keras-retinanet) and all its dependencies. It is recommended to create a 
virtual environment and install the dependencies using the following command. 

```python
pip install -r requirementsRetinaNet.txt
```

The [requirementsRetinaNet](../code/mask-rcnn/requirementsRetinaNet.txt) can be found in the code folder. 

## Folder structure

Create a folder ``retinanetmodels``, and organize your dataset with the following structure.

```bash
retinanetmodels
└── mydataset
    ├── annotations
    │   ├── 00001.xml
    │   ├── 00002.xml
    │   ├── 00003.xml
    │   ├── ...
    ├── images
    │   ├── 00001.jpg
    │   ├── 00002.jpg
    │   ├── 00003.jpg
    │   ├── ...
    ├── snapshots
    └── train.txt
```
The images must be annotated using the Pascal VOC dataset (xml files of the ``annotations`` folder). A tool for annotating images using this format is [LabelImg](https://github.com/tzutalin/labelImg). The ``train.txt`` must contain the list of images (without their extension) available in the ``images`` folder. Finally, ``snapshots`` is an empty folder where the weights of the models will be stored. 

## Necessary files

In order to fine-tune a model using this algorithm, it is necessary to download the following files in the folder ``retinanetmodels``:
- [TableBank weights](https://www.dropbox.com/s/rx5zlz3ovywddlh/resnet50_csv_15.h5?dl=1).
- [Dataset builder](../code/retinanet/build_dataset.py)

## Training

First of all, it is necessary to prepare the dataset using the [dataset builder file](../code/retinanet/build_dataset.py) by executing:

```python
python build_dataset.py -b mydaset
```

You should end up with the following structure:
```bash
retinanetmodels
└── mydataset
    ├── annotations
    │   ├── 00001.xml
    │   ├── 00002.xml
    │   ├── 00003.xml
    │   ├── ...
    ├── images
    │   ├── 00001.jpg
    │   ├── 00002.jpg
    │   ├── 00003.jpg
    │   ├── ...
    ├── resnet50_csv_15.h5  
    ├── retinanet_train.csv
    ├── retinanet_classes.csv
    ├── snapshots
    └── train.txt
```

Then, the model can be trained by executing:

```bash
python retinanet-train --batch-size 4 --steps <steps> --epochs <epochs> --weights resnet50_csv_15.h5 --multi-gpu-force --multi-gpu 2 --snapshot-path mydataset/snapshots csv retinanet_train.csv retinanet_classes.csv
```
It is necessary to change the value of ``<steps>`` by the number of images of the datased divided by 4, and ``<epochs>`` by the number of epochs that the model will be trained. 


The weights of the models will be stored in the  ``snapshots`` folder. You can use the models created in there using the [RetinaNet notebook](https://colab.research.google.com/drive/1Zgu7v7jLAKe-xITDbhBe9EDdCUozW-OB) or the [predict file](./code/retinanet/predict.py) only by changing the weights files, but first it is necessary to convert the weights of the model following the instructions of the [RetinaNet page](https://github.com/fizyr/keras-retinanet#converting-a-training-model-to-inference-model).



