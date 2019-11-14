# Close-Domain fine-tuning for table detection

In this project, we show the benefits of using models trained on a close domain, using the [TableBank dataset](https://github.com/doc-analysis/TableBank), for fine-tuning table detection models. In addition, we provide all the tools for using the constructed models, and fine-tune new detection models with custom datasets. 


## TableBank

We have started by training several models for the TableBank dataset. All the models, results, and tools are available in the [TableBank page](TableBank.md) of this repository. 

## Colab Notebooks for prediction
You can use the trained models with the following notebooks. 

- [MaskRCNN Notebook](https://colab.research.google.com/drive/1smseOGcUZZjvMfDHnoW8-ancldz-zpOg)
- [RetinaNet Notebook](https://colab.research.google.com/drive/1Zgu7v7jLAKe-xITDbhBe9EDdCUozW-OB)
- [SSD Notebook](https://colab.research.google.com/drive/1s8xoKf1gk0Aqs324genSCXXNVG3R-wJc)
- [YOLO Notebook](https://colab.research.google.com/drive/19x3FL2vUjF0as6CKrYKmjrqsiiUTjkw6)

## Model Zoo for table detection

From the models constructed with the TableBank dataset, we have fine-tuned models for table detection in different sources. All the information about this process is explained in the [Model Zoo for table detection page](ModelZoo.md) where we show the benefits of applying fine-tuning models generated from the TableBank dataset compared to models trained with natural images.   

## Fine-tuning

We provide the necessary tools to create custom table detection models using as a basis the models that we have constructed using the TableBank dataset. The instructions are provided in the [Fine-tuning page](FineTuning.md). 

## Citation

Use this bibtex to cite this work:

```
@misc{CasadoGarcia19,
  title={The Benefits of Close-Domain Fine-Tuning for Table Detection in Document Images},
  author={A. Casado-García and C. Domínguez and J. Heras and E. Mata and V. Pascual},
  year={2019},
  note={\url{https://github.com/holms-ur/fine-tuning/}},
}
```
## Acknowledgments
This work was partially supported by Ministerio de Economía y Competitividad [MTM2017-88804-P], Ministerio de Ciencia, Innovación y Universidades [RTC-2017-6640-7], Agencia de Desarrollo Econ\'omico de La Rioja [2017-I-IDD-00018], and the computing facilities of Extremadura Research Centre for Advanced Technologies (CETA-CIEMAT), funded by the European Regional Development Fund (ERDF). CETA-CIEMAT belongs to CIEMAT and the Government of Spain.


        
      
