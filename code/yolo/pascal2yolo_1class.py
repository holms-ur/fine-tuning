
# coding: utf-8

# Para ejecutar el script invocar a:
# 
# ```python pascal2yolo_1class -d <dir>```
# 
# donde ``<dir>`` es el path absoluto (sin el / final) donde se encuentran las imágenes las anotaciones en formato pascal voc.

# Cargamos lo primero las librerías que vamos a necesitar.

# In[35]:


import xml.etree.ElementTree as ET
import os
import argparse
from imutils import paths
import cv2
#import tqdm


# ### Código para transformar ficheros PascalVOC a YOLO
# 
# Función para extraer los cuadros de un fichero en formato pascal voc.

# In[19]:


def boxesFromPascalVOC(labelPath):
    tree = ET.parse(labelPath)
    root = tree.getroot()
    objects = root.findall('object')
    if(len(objects)<1):
        return None
    boxes = []
    for object in objects:
        category = object.find('name').text
        bndbox = object.find('bndbox')
        x  = int(bndbox.find('xmin').text)
        y = int(bndbox.find('ymin').text)
        h = int(bndbox.find('ymax').text)-y
        w = int(bndbox.find('xmax').text) - x
        boxes.append((category, (x, y, w, h)))
    return boxes


# Transformar un box de PascalVOC a YOLO.

# In[30]:


def transformPascalVOCBox2YOLO(wI,hI,box):
    objectClass = 0
    (_,(x,y,w,h))=box
    x = float(x)
    y = float(y)
    w = float(w)
    h = float(h)
    return (objectClass, (x+w/2)/wI, (y+h/2)/hI,w/wI,h/hI)    


# Transformar fichero PascalVOC asociado a una imagen a YOLO, la función toma como parámetro la imagen (debe haber un fichero anotado con el mismo nombre en la misma carpeta pero con extensión xml) y la carpeta de salida. 

# In[39]:


def transformPascalVOCFile2YOLO(imagePath,outputPath):
    img = cv2.imread(imagePath)
    filename = imagePath[imagePath.rfind("/")+1:imagePath.rfind(".")]
    labelPath = imagePath[0:imagePath.rfind(".")]+".xml"
    (H,W) = img.shape[:2]
    boxes = boxesFromPascalVOC(labelPath)
    imagePathsFileName = outputPath + filename + ".txt"
    imagePathsFile = open(imagePathsFileName,"w")
    if boxes is None:
        imagePathsFile.write("\n")
    else:
        for box in boxes:
            newbox = transformPascalVOCBox2YOLO(W,H,box)
            (c,x,y,w,h) = newbox
            imagePathsFile.write(str(c) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")
    imagePathsFile.close()


# ### Función para generar el fichero con la lista de imágenes. 

# In[16]:


def generateImagesFile(datasetPath):
    imagePathsFileName = datasetPath[0:datasetPath.rfind("/")+1]+"images.txt"
    imagePathsFile = open(imagePathsFileName,"w") 
    img_files = list(paths.list_files(datasetPath, validExts=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")))
    for img_file in img_files:
        imagePathsFile.write(img_file)
        imagePathsFile.write("\n")
    imagePathsFile.close()


# ### Para leer el path del dataset como un parámetro del script. 

# In[ ]:


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,help="path to the dataset of images")
args = vars(ap.parse_args())


# In[5]:


datasetPath= args["dataset"]
#datasetPath = "/media/jonathan/Elements/Estomas/dataset"


# Generamos fichero con lista de imágenes

# In[17]:


generateImagesFile(datasetPath)


# Creamos la carpeta donde se guardarán las anotaciones

# In[41]:


labelsPath = datasetPath[0:datasetPath.rfind("/")+1]+"labels/"


# In[42]:


#os.makedirs(labelsPath)


# Generamos las anotaciones

# In[43]:


img_files = list(paths.list_files(datasetPath, validExts=(".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")))
for img_file in img_files:
    transformPascalVOCFile2YOLO(img_file,datasetPath)


# In[ ]:




