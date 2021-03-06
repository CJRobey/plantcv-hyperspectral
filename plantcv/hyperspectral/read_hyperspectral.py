import os
from plantcv.plantcv import fatal_error
from plantcv.plantcv import params
from spectral import *

def read_hyperspectral(path):
    """this function allows you read in hyperspectral images in raw format (needs associated .hdr file)

    Inputs:
    path     = path to .hdr file, there is the assumption that .hdr file name matches raw image name

    Returns:
    hyperimge = image mask
    bands = band centers
    path = path to hyperspectral image
    filename = name of hyperspectral image

    :param hyperimg: spectral object
    :param bands: list of band centers
    :param path: string
    :return filname: string
    """

    params.device += 1

    if path.endswith(".hdr") == False:
        fatal_error("Input is not an .hdr file")
    if os.path.isfile(path) == False:
        fatal_error(str(path) + " does not exist")

    path1, filename = os.path.split(path)
    hyperimg = spectral.open_image(path)
    bands = hyperimg.bands.centers

    if params.debug == "print":
        message = str(filename) + "_input_image.png" + " succesfully opened. With a total of " + str(
            len(bands)) + " bands."
        print(message)
    elif params.debug == "plot":
        message = str(filename) + "_input_image.png" + " succesfully opened. With a total of " + str(
            len(bands)) + " bands."
        print(message)

    return hyperimg, bands, path, filename