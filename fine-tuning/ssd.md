# Fine tuning with the SSD algorithm.

## Installation 

Install the [GluonCV toolkit](https://gluon-cv.mxnet.io/). It is recommended to create a 
virtual environment and install the dependencies using the following command. 

```python
pip install -r requirementsSSD.txt
```

The [requirementsSSD](../code/ssd/requirementsSSD.txt) can be found in the code folder. 

## Folder structure

Create a folder ``ssdmodels`` and inside of it a folder called ``datasets``, and organize your dataset with the following structure. It is important that the name of your dataset starts with the prefix ``VOC``.

```bash
ssdmodels
├── configs
│   └── mydataset_config.py
└── datasets
    └── VOCmydataset
        ├── Annotations
        │   ├── 00001.xml
        │   ├── 00002.xml
        │   ├── 00003.xml
        │   ├── ...
        ├── ImageSets
        │   └── Main
        │       └── train.txt
        └── JPEGImages
            ├── 00001.jpg
            ├── 00002.jpg
            ├── 00003.jpg
            ├── ...
```
The images must be annotated using the Pascal VOC dataset (xml files of the ``Annotations`` folder). A tool for annotating images using this format is [LabelImg](https://github.com/tzutalin/labelImg). The ``train.txt`` must contain the list of images (without their extension) available in the ``JPEGImages`` folder. Finally, the file ``mydataset_config.py`` contains the configuration. In particular, the following options must be provided:

``python
classes = ['table']  
datasetName = 'mydataset'
nepochs = 200
``

You only need to change ``mydataset`` with the name of your dataset. 

## Necessary files

In order to fine-tune a model using this algorithm, it is necessary to download the following files in the folder ``ssdmodels``:
- [TableBank weights](https://www.dropbox.com/s/x95ipfjqoncrzt4/ssd_512_resnet50_tablebank_19.params?dl=0).
- [Dataset builder](../code/ssd/finetune_detection_transfer.py)

## Training

You can train the model by using the following command. 

```bash
python finetune_detection_transfer.py -c mydataset_config
```


The weights of the models will be stored in the  same folder where you are executing the above instruction. You can use the models created in there using the [SSD notebook](https://colab.research.google.com/drive/1s8xoKf1gk0Aqs324genSCXXNVG3R-wJc) or the [predict file](./code/ssd/predict.py).



