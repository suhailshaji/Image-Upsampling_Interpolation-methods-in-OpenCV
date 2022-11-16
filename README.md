# Image-Upsampling_Interpolation-methods-in-OpenCVINTERPOLATION METHODS USING OPENCV

METHODS
1.INTER_AREA
2.INTER_NEAREST
3.INTER_LINEAR
4.INTER-LINEAR-EXACT
5.INTER_CUBIC


1.INTER_AREA
INTER_AREA works better in image decimation and avoiding false inference patterns in images.


ORIGINAL IMAGE


RESULT



2. INTER_NEAREST
Nearest neighbor interpolation algorithm. It retains the sharpness of the edges though the overall image may be blurred.

RESULT



3. INTER_LINEAR
 INTER_NEAREST, this does the interpolation in two dimensions and predicts the function used to calculate the color of a pixel.
This algorithm is effective in handling visual distortions while zooming or enlarging an image.


RESULT



4. INTER_LINEAR_EXACT
INTER_LINEAR_EXACT is a modification of INTER_LINEAR and both uses bilinear interpolation algorithm. The only difference is that the calculations in INTER_LINEAR_EXACT are accurate to a bit.

RESULT


5. INTER_CUBIC
This option uses bicubic interpolation technique. This is an extension of cubic interpolation technique and is used for 2 dimension regular grid patterns.


RESULT –NOT GOOD

OTHER METHODS
    1. NTER_LANCZOS4
    2. INTER_MAX
    3. WARP_FILL_OUTLIERS
    4. WARP_INVERSE_MAP



CODE

SCALE PRECENTAGE 220 


Tried with higher scale 






DIRECT APPROCH BICUBIC INTERPOLATION
Result

Code



