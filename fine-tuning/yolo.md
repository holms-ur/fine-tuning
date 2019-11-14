# Fine tuning with the YOLO algorithm.

## Installation 

Install the [Darknet library](https://pjreddie.com/darknet/yolo/):

```python
git clone https://github.com/AlexeyAB/darknet
cd darknet
make
``` 

## Folder structure

Create a folder ``datasets`` inside the ``darknet`` folder and inside of it a folder called ``mydataset``, and organize your dataset with the following structure. It is important that the name of your dataset starts with the prefix ``VOC``.

```bash
darknet
└── datasets
    └── mydataset
        └── train
            └── JPEGImages
                ├── 00001.jpg
                ├── 00001.xml
                ├── 00002.jpg                
                ├── 00002.xml
                ├── 00003.jpg                                
                ├── 00003.xml
                └── ...
```
The images must be annotated using the Pascal VOC dataset. A tool for annotating images using this format is [LabelImg](https://github.com/tzutalin/labelImg). 
Initially, all the images and annotations must be stored in the same folder. We need to convert the images to the YOLO format using the following python script 
that requires the [pascal2yolo file](../code/yolo/pascal2yolo_1class.py) that should be downloaded in the ``yolomodels`` folder:

``bash
python pascal2yolo_1class.py -d datasets/mydataset/train/JPEGImages 
``

This produces the following file structure
```bash
darknet
└── datasets
    └── mydataset
        └── train
            └── JPEGImages
                ├── 00001.jpg
                ├── 00001.txt
                ├── 00001.xml
                ├── 00002.jpg
                ├── 00002.txt
                ├── 00002.xml
                ├── 00003.jpg                                
                ├── 00003.txt
                ├── 00003.xml
                └── ...
```

You have to move the generated .txt files to a ``labels`` folder:

```bash
darknet
└── datasets
    └── mydataset
        └── train
            ├── JPEGImages
            │   ├── 00001.jpg
            │   ├── 00001.xml
            │   ├── 00002.jpg
            │   ├── 00002.xml
            │   ├── 00003.jpg                                
            │   ├── 00003.xml
            │   └── ...
            │   
            └── labels
                ├── 00001.txt
                ├── 00002.txt
                ├── 00003.txt  
                └── ...
```

Finally, you need to generate a txt with the list of files. From the darknet folder execute the following command.

``bash
find `pwd`/datasets/mydataset/train/JPEGImages/*.jpg > datasets/mydataset/train.txt
``

## Necessary files

In order to fine-tune a model using this algorithm, it is necessary to download the following files in the folder ``yolomodels``:
- [TableBank weights](https://www.dropbox.com/s/jbgosn1t83h1bqi/tablasFinaltrain_10000.weights?dl=1).
- [Configuration file](../code/yolo/tablasFinaltest416320.cfg)
- [Names file](../code/yolo/vocTablas.names)
- [Data file](../code/yolo/tablasFinal.data)

If you have given a name to your dataset (folder ``mydataset``, you need to modify the [data file](../code/yolo/tablasFinal.data) 
with the name of your dataset. 

## Training

You can train the model by using the following command from the darknet folder. 

```bash
darknet detector train tablasFinal.data tablasFinaltest416320.cfg tablasFinaltrain_10000.weights
```

The weights of the models will be stored in the ``backup`` folder of the ``darknet`` directory. 
You can use the models created in there using the [YOLO notebook](https://colab.research.google.com/drive/19x3FL2vUjF0as6CKrYKmjrqsiiUTjkw6)
or the [predict file](./code/yolo/predict.py).



