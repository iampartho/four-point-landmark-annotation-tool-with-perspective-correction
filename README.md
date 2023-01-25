## This repository is a four-point land-mark annotation app which can be used to annotate images and also using those annotated point the perspectives are corrected

## Requirements

* Opencv-python
* Numpy

## How to run the code

1. First you need to modify the code **annotate.py** in order to specify the root folder where all the images are kept. You need to change the **line 77** in the code to specify the root path as a parameter into the **main()** function.
2. Then you have to run the following code into your terminal/command prompt
```
python annotate.py
```
3. A cv2 image showing window will open visualizing the image. By left clicking it you can put a landmark, by right clicking you can undo the landmark. After giving four landmark you can press "S" to save the annotation and the next image will come in the window. You can press "E" to exit the annotation app.
4. When you save an annotation the annotations are normalised and saved into a folder named annotated_files in a txt file along with the image (the image is moved to that folder). The txt file name is the same as the image file name
5. Additionally, if you want to correct the perspective of an image by the landmark annotated you can use the code name **visualizing_the_image_after_annotating.py** to visualize it.
6. For that you need to edit the code first on **line 9** where you need to specify the root image folder path into **img_folder** variable. 
7. Then you have to run the following code into your terminal/command prompt
```
python visualizing_the_image_after_annotating.py
```
8. A cv2 window will open up by correcting the perspective of the image by using the landmark annotation
9. If you feel okay with the annotation you can press "N" to see the next perspective corrected image or you can press "R" to redo the landmark. By pressing N the image and the annotation will be moved to *finalized* named directory where the code is situated. By pressing "R" the image along with the annotation will be moved to the folder where the **img_folder** variable is locating. You can also press "E" to exit the window.
