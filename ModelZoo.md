# Model Zoo for table detection

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

## Fine-tuning from natural images

From models trained with the Pascal VOC dataset, we have created several detection models for the aforementioned datasets using fine-tuning with the algorithms Mask-RCNN, RetinaNet, SSD and YOLO. The results are summarized in the following figure.

![Results transfer learning from natural images](images/das.png)

The trained models are available in the format used by each framework, and distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

|| Mask RCNN|RetinaNet|SSD|YOLO|
|----------|----------|----------|----------|----------|
|ICDAR13| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EU0QwvNmCEtGlu4JSbAP9gQBsR9KIjxQJJLIML6cDy380A?e=L2KNyY), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/ETMmVrsbVcdGse4R-fOhkocBzJjrIMzaxgn_ovzm7dRteQ?e=k0Okzg), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17FIG| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/Eeg-oEPdxl5PuQyjqNedGpMBaYLryQSPZp9HOO6S8acqaQ?e=vVHTsf), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17FOR| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EX004aBDx0ZGsM4QfX9PoCsBzPddsr38A8A3mIGpSiROLw?e=xWwbFg), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR19| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|Invoices| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EVqiaX3VgVZLmTbUBe0kRbQBCf0r1peyo5d_8k3YYJg3FQ?e=R6ZGA3), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|MarmotChi| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EeypoDUR2TxPqKoymbZJxNsBYwocn1F_cTikDXKBk1iKhg?e=ET6CAV), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|MarmotEn| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EXq35-moQl1MoM_PM5VuJE4BLjeXAET7mXfGmUNIRtmiVg?e=asCckz), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|UNLV| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EVA4H2k4O4ZDvO-SlYE5l0wBS0L_7_KOXNI9_RmVQvcQfw?e=5dGGZS), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|


## Fine-tuning from the TableBank dataset

From models trained with the TableBank dataset, we have created several detection models for the aforementioned datasets using fine-tuning with the algorithms Mask-RCNN, RetinaNet, SSD and YOLO. The results are summarized in the following figure.

![Results transfer learning from the TableBank dataset](images/dasTrans.png)

The trained models are available in the format used by each framework, and distributed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

|| Mask RCNN|RetinaNet|SSD|YOLO|
|----------|----------|----------|----------|----------|
|ICDAR13| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EU2UHSi2X7ZHhUgkWVBZmcABDSbzxBL-cdXijp47gbrfLw?e=mXYm7i), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/ESh0c7AYAERFo1mW0jx5UtkB9sFrOyLIbCC8ZzKM4UWtXg?e=7BC2yA), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17FIG| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/Ee-xiC8-sTxMjKiLPGT0wcQBORVUlOpjFc81Q47ow4BOQQ?e=DMjCkX), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR17FOR| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EQL6UcTvV7ZHgsiZBptIMGEB-uMPAytxpEIPdPMIFF8OMg?e=eGq4cG), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|ICDAR19| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|Invoices| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EYrBpkAnuo5FjeH52SSS4o8BjYBXDbQ62b2U43xysw2Z1A?e=yLbe9L), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|MarmotChi| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/ESZGsuGCX0hCirvi1ueu62EBT_IIiHXhprKJiDIfoNXzvg?e=XIcu3a), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|MarmotEn| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/ES_T96i_HmBLqFL3d-vBUTUBHmwN7sJY4YBhxvqk9lApHw?e=jGdx0l), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|
|UNLV| [weights]()|[weights](),[classes file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/retinanet/retinanet_classes.csv)| [weights]() |  [weights](https://unirioja-my.sharepoint.com/:u:/g/personal/cedomin_unirioja_es/EYFwrK7aiaVDqYHLRqy_qqABTNdoiiwibRrKPVACJYbCvw?e=G0m8qg), [config file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/tablasFinaltest416320.cfg), [names file](https://raw.githubusercontent.com/holms-ur/fine-tuning/master/code/yolo/vocTablas.names)|

## Comparison of models

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
