# Fine tuning with the Mask RCNN algorithm.

## Installation 

Install the [Mask RCNN library](https://github.com/matterport/Mask_RCNN/) and all its dependencies. It is recommended to create a 
virtual environment and install the dependencies using the following command. 

```python
pip install -r requirementsMaskRCNN.txt
```

The [requirementsMaskRCNN](code/maskrcnn/requirementsMaskRCNN.txt) can be found in the code folder. 

## Folder structure

Organize your dataset with the following structure.

```bash
.
├── annots
│   ├── 00001.xml
│   ├── 00002.xml
│   ├── 00003.xml
│   ├── 00004.xml
│   ├── 00005.xml
│   ├── 00006.xml
│   ├── 00007.xml
│   ├── 00009.xml
│   ├── 00010.xml
│   ├── 00011.xml
│   ├── 00012.xml
│   ├── 00013.xml
│   ├── 00014.xml
│   ├── 00016.xml
│   ├── 00017.xml
│   ├── 00018.xml
│   ├── 00019.xml
│   ├── 00020.xml
│   ├── 00021.xml
│   ├── 00022.xml
│   ├── 00023.xml
│   ├── 00024.xml
│   ├── 00025.xml
│   ├── 00026.xml
│   ├── 00027.xml
│   ├── 00028.xml
│   ├── 00029.xml
│   ├── 00030.xml
│   ├── 00031.xml
│   ├── 00032.xml
│   ├── 00033.xml
│   ├── 00034.xml
│   ├── 00036.xml
│   ├── 00037.xml
│   ├── 00038.xml
│   ├── 00039.xml
│   ├── 00040.xml
│   ├── 00041.xml
│   ├── 00042.xml
│   ├── 00043.xml
│   ├── 00044.xml
│   ├── 00045.xml
│   ├── 00046.xml
│   ├── 00047.xml
│   ├── 00048.xml
│   ├── 00049.xml
│   ├── 00050.xml
│   ├── 00051.xml
│   ├── 00052.xml
│   ├── 00053.xml
│   ├── 00054.xml
│   ├── 00055.xml
│   ├── 00056.xml
│   ├── 00059.xml
│   ├── 00060.xml
│   ├── 00061.xml
│   ├── 00062.xml
│   ├── 00064.xml
│   ├── 00065.xml
│   ├── 00066.xml
│   ├── 00069.xml
│   ├── 00071.xml
│   ├── 00072.xml
│   ├── 00073.xml
│   ├── 00074.xml
│   ├── 00075.xml
│   ├── 00076.xml
│   ├── 00077.xml
│   ├── 00078.xml
│   ├── 00079.xml
│   ├── 00080.xml
│   ├── 00081.xml
│   ├── 00083.xml
│   ├── 00084.xml
│   ├── 00085.xml
│   ├── 00086.xml
│   ├── 00087.xml
│   ├── 00088.xml
│   ├── 00089.xml
│   ├── 00090.xml
│   ├── 00091.xml
│   ├── 00092.xml
│   ├── 00093.xml
│   ├── 00094.xml
│   ├── 00095.xml
│   ├── 00096.xml
│   ├── 00097.xml
│   ├── 00098.xml
│   ├── 00099.xml
│   ├── 00100.xml
│   ├── 00101.xml
│   ├── 00102.xml
│   ├── 00103.xml
│   ├── 00105.xml
│   ├── 00107.xml
│   ├── 00108.xml
│   ├── 00109.xml
│   ├── 00110.xml
│   ├── 00111.xml
│   ├── 00112.xml
│   ├── 00113.xml
│   ├── 00114.xml
│   ├── 00115.xml
│   ├── 00116.xml
│   ├── 00117.xml
│   ├── 00118.xml
│   ├── 00119.xml
│   ├── 00120.xml
│   ├── 00121.xml
│   ├── 00122.xml
│   ├── 00123.xml
│   ├── 00124.xml
│   ├── 00125.xml
│   ├── 00127.xml
│   ├── 00128.xml
│   ├── 00129.xml
│   ├── 00130.xml
│   ├── 00131.xml
│   ├── 00132.xml
│   ├── 00134.xml
│   ├── 00136.xml
│   ├── 00137.xml
│   ├── 00139.xml
│   ├── 00140.xml
│   ├── 00141.xml
│   ├── 00143.xml
│   ├── 00144.xml
│   ├── 00145.xml
│   ├── 00146.xml
│   ├── 00147.xml
│   ├── 00148.xml
│   ├── 00149.xml
│   ├── 00150.xml
│   ├── 00151.xml
│   ├── 00152.xml
│   ├── 00153.xml
│   ├── 00154.xml
│   ├── 00155.xml
│   ├── 00156.xml
│   ├── 00157.xml
│   ├── 00158.xml
│   ├── 00159.xml
│   ├── 00161.xml
│   ├── 00162.xml
│   ├── 00163.xml
│   ├── 00164.xml
│   ├── 00166.xml
│   ├── 00167.xml
│   ├── 00168.xml
│   ├── 00169.xml
│   ├── 00170.xml
│   ├── 00171.xml
│   ├── 00172.xml
│   ├── 00173.xml
│   ├── 00174.xml
│   ├── 00175.xml
│   ├── 00176.xml
│   ├── 00177.xml
│   ├── 00178.xml
│   ├── 00179.xml
│   ├── 00180.xml
│   ├── 00181.xml
│   ├── 00182.xml
│   └── 00183.xml
└── images
    ├── 00001.jpg
    ├── 00002.jpg
    ├── 00003.jpg
    ├── 00004.jpg
    ├── 00005.jpg
    ├── 00006.jpg
    ├── 00007.jpg
    ├── 00009.jpg
    ├── 00010.jpg
    ├── 00011.jpg
    ├── 00012.jpg
    ├── 00013.jpg
    ├── 00014.jpg
    ├── 00016.jpg
    ├── 00017.jpg
    ├── 00018.jpg
    ├── 00019.jpg
    ├── 00020.jpg
    ├── 00021.jpg
    ├── 00022.jpg
    ├── 00023.jpg
    ├── 00024.jpg
    ├── 00025.jpg
    ├── 00026.jpg
    ├── 00027.jpg
    ├── 00028.jpg
    ├── 00029.jpg
    ├── 00030.jpg
    ├── 00031.jpg
    ├── 00032.jpg
    ├── 00033.jpg
    ├── 00034.jpg
    ├── 00036.jpg
    ├── 00037.jpg
    ├── 00038.jpg
    ├── 00039.jpg
    ├── 00040.jpg
    ├── 00041.jpg
    ├── 00042.jpg
    ├── 00043.jpg
    ├── 00044.jpg
    ├── 00045.jpg
    ├── 00046.jpg
    ├── 00047.jpg
    ├── 00048.jpg
    ├── 00049.jpg
    ├── 00050.jpg
    ├── 00051.jpg
    ├── 00052.jpg
    ├── 00053.jpg
    ├── 00054.jpg
    ├── 00055.jpg
    ├── 00056.jpg
    ├── 00059.jpg
    ├── 00060.jpg
    ├── 00061.jpg
    ├── 00062.jpg
    ├── 00064.jpg
    ├── 00065.jpg
    ├── 00066.jpg
    ├── 00069.jpg
    ├── 00071.jpg
    ├── 00072.jpg
    ├── 00073.jpg
    ├── 00074.jpg
    ├── 00075.jpg
    ├── 00076.jpg
    ├── 00077.jpg
    ├── 00078.jpg
    ├── 00079.jpg
    ├── 00080.jpg
    ├── 00081.jpg
    ├── 00083.jpg
    ├── 00084.jpg
    ├── 00085.jpg
    ├── 00086.jpg
    ├── 00087.jpg
    ├── 00088.jpg
    ├── 00089.jpg
    ├── 00090.jpg
    ├── 00091.jpg
    ├── 00092.jpg
    ├── 00093.jpg
    ├── 00094.jpg
    ├── 00095.jpg
    ├── 00096.jpg
    ├── 00097.jpg
    ├── 00098.jpg
    ├── 00099.jpg
    ├── 00100.jpg
    ├── 00101.jpg
    ├── 00102.jpg
    ├── 00103.jpg
    ├── 00105.jpg
    ├── 00107.jpg
    ├── 00108.jpg
    ├── 00109.jpg
    ├── 00110.jpg
    ├── 00111.jpg
    ├── 00112.jpg
    ├── 00113.jpg
    ├── 00114.jpg
    ├── 00115.jpg
    ├── 00116.jpg
    ├── 00117.jpg
    ├── 00118.jpg
    ├── 00119.jpg
    ├── 00120.jpg
    ├── 00121.jpg
    ├── 00122.jpg
    ├── 00123.jpg
    ├── 00124.jpg
    ├── 00125.jpg
    ├── 00127.jpg
    ├── 00128.jpg
    ├── 00129.jpg
    ├── 00130.jpg
    ├── 00131.jpg
    ├── 00132.jpg
    ├── 00134.jpg
    ├── 00136.jpg
    ├── 00137.jpg
    ├── 00139.jpg
    ├── 00140.jpg
    ├── 00141.jpg
    ├── 00143.jpg
    ├── 00144.jpg
    ├── 00145.jpg
    ├── 00146.jpg
    ├── 00147.jpg
    ├── 00148.jpg
    ├── 00149.jpg
    ├── 00150.jpg
    ├── 00151.jpg
    ├── 00152.jpg
    ├── 00153.jpg
    ├── 00154.jpg
    ├── 00155.jpg
    ├── 00156.jpg
    ├── 00157.jpg
    ├── 00158.jpg
    ├── 00159.jpg
    ├── 00161.jpg
    ├── 00162.jpg
    ├── 00163.jpg
    ├── 00164.jpg
    ├── 00166.jpg
    ├── 00167.jpg
    ├── 00168.jpg
    ├── 00169.jpg
    ├── 00170.jpg
    ├── 00171.jpg
    ├── 00172.jpg
    ├── 00173.jpg
    ├── 00174.jpg
    ├── 00175.jpg
    ├── 00176.jpg
    ├── 00177.jpg
    ├── 00178.jpg
    ├── 00179.jpg
    ├── 00180.jpg
    ├── 00181.jpg
    ├── 00182.jpg
    └── 00183.jpg
```

