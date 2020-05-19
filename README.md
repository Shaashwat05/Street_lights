
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 

# Street_lights
 A system that understands the visuality of the environment using **raspberry pi** and camera. It uses the **HSV** image format to calculate hoe visually clear the image is. The using object detection with **YOLOV3** we find if any people are around for the light to remain on. If no then turn them off to conserve energy.

### Prerequisites

What things you need to install the software and how to install them

```
cv2
numpy 
matplotlib
time
os 
argparse
RPI
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above. Download the required files of YOLOV3. Then run main.py to capture an image and see its visuality, object detection output on it and power of LEDs.

```
$ main.py

```

## Cloning
```bash
$ git clone https://github.com/Shaashwat05/Street_lights
```

## Decrypted Image
The output image and power of street lights required can be seen.

![The input Image to cartoonize.py](https://github.com/Shaashwat05/Street_lights/blob/master/output.png)


## Built With

* [python](https://www.python.org/) - The software used

## Authors
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)       [![Github-profile](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Shaashwat05)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) 

## Acknowledgments

* Hat tip to anyone whose code was used

