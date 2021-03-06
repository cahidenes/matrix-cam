# Matrix Cam
Applies matrix effect to camera with OpenCV using Python

![Demo of the output](https://raw.githubusercontent.com/cahidenes/visuals/main/matrix.gif)

There are many parameters that you can play with in `parameters.py`. Here is an example with different parameters:

![Another demo](https://github.com/cahidenes/visuals/blob/main/matrix.png?raw=true)

## Usage

You need OpenCV and Pillow to run the program. To install all dependencies run: 

```sh
pip install -r requirements.txt
```

## Cam To Matrix

To direct camera to the program, use `camToMatrix.py`.

    python3 camToMatrix.py
    
## Image To Matrix

To direct image to the program, use `imageToMatrix.py`

    python3 imageToMatrix.py input_image.jpg output_image.jpg
    
## Video To Matrix

To direct video to the program, use `videoToMatrix.py`

    python3 videoToMatrix.py input_video.mp4 output_video_name

**Warning:** Output video does not work on some machines.

## Parameters

Play with parameters in `parameters.py` file. Read comments for more information.

*Feel free to use this project in your projects, comment or contribute.*
