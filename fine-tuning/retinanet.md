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
    └── snapshots
```
The images must be annotated using the Pascal VOC dataset (xml files of the ``annots`` folder). A tool for annotating images using this format is [LabelImg](https://github.com/tzutalin/labelImg).

## Necessary files

In order to fine-tune a model using this algorithm, it is necessary to download the following files in the folder ``retinanetmodels``:
- [TableBank weights](https://www.dropbox.com/s/dcl53rl3xqndfdx/mask_rcnn_tablebank_cfg_0002.h5?dl=1).
- [Dataset builder](../code/retinanet/build_dataset.py)

## Training

First of all, it is necessary to modify the template file downloaded in the previous step. Just search the text ``<- MODIFY ->``  in the template file and follow the instructions. To train the model execute the following command in the folder ``retinanetmodels``:

```python
python template.py
```

The weights of the models will be stored in a folder called ``model_cfg``. You can use the models created in there using the [Mask RCNN notebook](https://colab.research.google.com/drive/1Zgu7v7jLAKe-xITDbhBe9EDdCUozW-OB) or the [predict file](./code/retinanet/predict.py) only by changing the weights files. 



