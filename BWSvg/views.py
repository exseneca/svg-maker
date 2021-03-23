from PIL import Image, ImageOps
import os
from django.contrib import settings
import numpy as np
from potrace import Bitmap
from django.shortcuts import render



def home(request):
    # use the dummy picture and pass in list of 256
    # images
    FILE_NAME = 'spermwhale.jpg'
    #url = staticfiles_storage.url('spermwhale.jpg')
    stc_rt = settings.STATIC_ROOT
    file_path = os.path.join(settings.STATIC_ROOT, 'BWSvg', FILE_NAME)

#THRESHOLD = 75
    im = Image.open(url).convert('L')
    return render(request, 'BWSvg/home.html')

#def upload(request):
# need to take a post request of 
# file upload, then run the home
# function with this new uploaded file

#def download(request):
# reverse the image held in the current threshol
# 