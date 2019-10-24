# Fine tuning with the Mask RCNN algorithm.

## Installation 

Install the [Mask RCNN library](https://github.com/matterport/Mask_RCNN/) and all its dependencies. It is recommended to create a 
virtual environment and install the dependencies using the following command. 

```python
pip install -r requirementsMaskRCNN.txt
```

The [requirementsMaskRCNN](code/maskrcnn/requirementsMaskRCNN.txt) can be found in the code folder. 

## Folder structure

Create a folder ``maskrcnnmodels``, and organize your dataset with the following structure.

```bash
maskrcnnmodels
└── mydataset
    ├── annots
    │   ├── 00001.xml
    │   ├── 00002.xml
    │   ├── 00003.xml
    │   ├── ...
    └── images
        ├── 00001.jpg
        ├── 00002.jpg
        ├── 00003.jpg
        ├── ...
```
The images must be annotated using the Pascal VOC dataset (xml files of the ``annots`` folder). A tool for annotating images using this format is [LabelImg](https://github.com/tzutalin/labelImg).

## Necessary files

In order to fine-tune a model using this algorithm, it is necessary to download the following files in the folder ``maskrcnnmodels``:
- [TableBank weights](https://www.dropbox.com/s/dcl53rl3xqndfdx/mask_rcnn_tablebank_cfg_0002.h5?dl=1).
- [Template training file](code/maskrcnn/template.py)

## Training

First of all, it is necessary to modify the template file downloaded in the previous step. Just search the text ``<- MODIFY ->``  in the template file and follow the instructions. To train the model execute the following command in the folder ``maskrcnnmodels``:

```python
python template.py
```

The models will be stored in a folder called ``model_cfg``. You can use the models created in there using the [Mask RCNN notebook](https://colab.research.google.com/drive/1smseOGcUZZjvMfDHnoW8-ancldz-zpOg) only by changing the weights files. 



