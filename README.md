# Close-Domain fine-tuning for table detection

In this project, we show the benefits of using models trained on a close domain, using the [TableBank dataset](https://github.com/doc-analysis/TableBank), for fine-tuning table detection models. In addition, we provide all the tools for using the constructed models, and fine-tune new detection models with custom datasets. 


## TableBank

We have trained several models for the LaTeX part of the TableBank dataset using the [Mask-RCNN](https://arxiv.org/abs/1703.06870), [RetinaNet](https://arxiv.org/abs/1708.02002), [SSD](https://arxiv.org/abs/1512.02325) and [YOLO](https://arxiv.org/abs/1804.02767) algorithms using different deep learning libraries. To this aim, we have used several libraries: 
- [Keras library for Mask RCNN](https://github.com/matterport/Mask_RCNN/)
- [Keras library for RetinaNet](https://github.com/fizyr/keras-retinanet)
- [Implementation of SSD in MXNet](https://gluon.mxnet.io/chapter08_computer-vision/object-detection.html)
- [Implementation of YOLO in Darknet](https://github.com/AlexeyAB/darknet)

### Results

To evaluate our models, we have employed the same metric used in the [ICDAR 2019 Competition on Table Detection](http://sac.founderit.com/evaluation.html). 

|Model|P@0.6|R@0.6|F1@0.6|P@0.7|R@0.7|F1@0.7|P@0.8|R@0.8|F1@0.8|P@0.9|R@0.9|F1@0.9|  WAvgF1|
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|Mask RCNN|0,94|0,98|0,96|0,94|0,97|0,95|0,93|0,96|0,94|0,84|0,87|0,86|0,92|
|RetinaNet |0,98|0,86|0,92|0,98|0,86|0,92|0,97|0,85|0,91|0,94|0,82|0,87|0,90|
|SSD |0,96|0,97|0,96|0,94|0,95|0,95|0,92|0,92|0,92|0,82|0,82|0,82|0,90|
|YOLO |0,98|0,99|0,98|0,98|0,99|0,98|0,96|0,97|0,96|0,74|0,75|0,75|0,90|

### Model Zoo

The trained models are available in the format used by each framework, and distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

- Mask RCNN: [weights](https://www.dropbox.com/s/dcl53rl3xqndfdx/mask_rcnn_tablebank_cfg_0002.h5?dl=1).
- RetinaNet: [weights](https://www.dropbox.com/s/iwve914qp6d2nmy/output.h5?dl=1), [classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- SSD: [weights](https://www.dropbox.com/s/x95ipfjqoncrzt4/ssd_512_resnet50_tablebank_19.params?dl=1).
- YOLO: [weights](https://www.dropbox.com/s/jbgosn1t83h1bqi/tablasFinaltrain_10000.weights?dl=1), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).

### Colab Notebooks for prediction
You can use the trained models with the following notebooks. 

- [MaskRCNN Notebook](https://colab.research.google.com/drive/1smseOGcUZZjvMfDHnoW8-ancldz-zpOg)
- [RetinaNet Notebook](https://colab.research.google.com/drive/1Zgu7v7jLAKe-xITDbhBe9EDdCUozW-OB)
- [SSD Notebook](https://colab.research.google.com/drive/1s8xoKf1gk0Aqs324genSCXXNVG3R-wJc)
- [YOLO Notebook](https://colab.research.google.com/drive/19x3FL2vUjF0as6CKrYKmjrqsiiUTjkw6)


## Model Zoo for table detection

We have trained several models for the following datasets: [ICDAR13](http://www.tamirhassan.com/html/competition.html), [ICDAR17](http://u-pat.org/ICDAR2017/program_competitions.php) (this dataset is used to construct models for detecting tables, figures and formulas), [ICDAR19 modern images](http://sac.founderit.com/), Invoices (a private dataset that is available under request), [Marmot Chinese](http://www.icst.pku.edu.cn/cpdp/sjzy/index.htm), [Marmot English](http://www.icst.pku.edu.cn/cpdp/sjzy/index.htm) and [UNLV](https://dl.acm.org/citation.cfm?id=1815345). Since these datasets do not provide a publicly available test set; we have split the training sets using the partition 75% for training and 25% for testing. The dataset splits are available as follows. 


- ICDAR13: [train set](splits/icdar13-train.txt), [test set](splits/icdar13-test.txt).
- ICDAR17: [train set](splits/icdar17-train.txt), [test set](splits/icdar17-test.txt).
- ICDAR17FIG: [train set](splits/icdar17-train.txt), [test set](splits/icdar17-test.txt).
- ICDAR17FOR: [train set](splits/icdar17-train.txt), [test set](splits/icdar17-test.txt).
- ICDAR19: [train set](splits/icdar19-train.txt), [test set](splits/icdar19-test.txt).
- Invoices: [train set](splits/invoices-train.txt), [test set](splits/invoices-test.txt).
- MarmotChi: [train set](splits/marmotChi-train.txt), [test set](splits/marmotChi-test.txt).
- MarmotEn: [train set](splits/marmotEn-train.txt), [test set](splits/marmotEn-test.txt).
- UNLV: [train set](splits/unlv-train.txt), [test set](splits/unlv-test.txt).

### Fine-tuning from natural images

From models trained with the Pascal VOC dataset, we have created several detection models for the aforementioned datasets using fine-tuning with the algorithms Mask-RCNN, RetinaNet, SSD and YOLO. The results are summarized in the following figure.

![Results transfer learning from natural images](images/das.png)

The trained models are available in the format used by each framework, and distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

#### Mask RCNN
- ICDAR13: [weights]().
- ICDAR17: [weights]().
- ICDAR17FIG: [weights]().
- ICDAR17FOR: [weights]().
- ICDAR19: [weights]().
- Invoices: [weights]().
- MarmotChi: [weights]().
- MarmotEn: [weights]().
- UNLV: [weights]().


#### RetinaNet
- ICDAR13: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17FIG: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17FOR: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR19: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- Invoices: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- MarmotChi: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- MarmotEn: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- UNLV: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).

#### SSD
- ICDAR13: [weights]().
- ICDAR17: [weights]().
- ICDAR17FIG: [weights]().
- ICDAR17FOR: [weights]().
- ICDAR19: [weights]().
- Invoices: [weights]().
- MarmotChi: [weights]().
- MarmotEn: [weights]().
- UNLV: [weights]().

#### YOLO

- ICDAR13: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17FIG: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17FOR: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR19: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- Invoices: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- MarmotChi: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- MarmotEn: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- UNLV: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).

### Fine-tuning from the TableBank dataset

From models trained with the TableBank dataset, we have created several detection models for the aforementioned datasets using fine-tuning with the algorithms Mask-RCNN, RetinaNet, SSD and YOLO. The results are summarized in the following figure.

![Results transfer learning from the TableBank dataset](images/dasTrans.png)

The trained models are available in the format used by each framework, and distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

#### Mask RCNN
- ICDAR13: [weights]().
- ICDAR17: [weights]().
- ICDAR17FIG: [weights]().
- ICDAR17FOR: [weights]().
- ICDAR19: [weights]().
- Invoices: [weights]().
- MarmotChi: [weights]().
- MarmotEn: [weights]().
- UNLV: [weights]().


#### RetinaNet
- ICDAR13: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17FIG: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR17FOR: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- ICDAR19: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- Invoices: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- MarmotChi: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- MarmotEn: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).
- UNLV: [weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv).

#### SSD
- ICDAR13: [weights]().
- ICDAR17: [weights]().
- ICDAR17FIG: [weights]().
- ICDAR17FOR: [weights]().
- ICDAR19: [weights]().
- Invoices: [weights]().
- MarmotChi: [weights]().
- MarmotEn: [weights]().
- UNLV: [weights]().

#### YOLO

- ICDAR13: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17FIG: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR17FOR: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- ICDAR19: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- Invoices: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- MarmotChi: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- MarmotEn: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).
- UNLV: [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names).

### Comparison of models

In the next table, we compare the [WF1Avg score](http://sac.founderit.com/evaluation.html) obtained by the models fine-tuned from models constructed using natural images, and the models constructed using the TableBank dataset.

||Mask R-CNN Natural| Mask R-CNN TableBank |RetinaNet Natural| RetinaNet TableBank |SSD Natural| SSD TableBank |YOLO Natural| YOLO TableBank |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|ICDAR13|0.09|0.72|0.5|0.74|0.4|0.52|0.50|0.66|
|ICDAR17|0.27|0.72|0.66|0.84|0.45|0.47|0.72|0.82|
|ICDAR17FIG|0.19|0.29|0.72|0.72|0.59|0.29|0.63|0.71|
|ICDAR17FOR|0.09|0.06|0.1|0.2|0.32|0.35|0.52|0.59|
|ICDAR19|0.31|0.65|0.64|0.72|0.2|0.23|0.81|0.85|
|Invoices|0.22|0.44|0.65|0.66|0.59|0.66|0.63|0.69|
|MarmotChi|0.21|0.70|0.69|0.84|0.58|0.64|0.7|0.87|
|MarmotEn|0.39|0.82|0.70|0.8|0.44|0.45|0.83|0.85|
|UNLV|0.15|0.55|0.73|0.74|0.42|0.49|0.7|0.77|


## Fine-tuning

We provide the necessary tools to create your custom table detection models using as a basis the models that we have constructed using the TableBank dataset. 



        
      
