from PIL import Image, ImageOps
import os
from io import BytesIO
from django.conf import settings
import numpy as np
from potrace import Bitmap
from django.shortcuts import render
from .models import BeforeImage, AfterImage
from django.core.files.base import ContentFile
import logging

def create_bit_image(im, threshold):
    threshold_fn = lambda x : 255 if x > threshold else 0
    return im.point(threshold_fn, mode='1')


def home(request):
    # use the dummy picture and pass in list of 256
    # images
    logger = logging.getLogger(__name__)
    BEFORE_FILE_NAME = 'spermwhale'
    before_img = BeforeImage.objects.get(name=BEFORE_FILE_NAME).img
    before_img_url = before_img.url

    AFTER_FILE_NAME = 'after-image'
    after_img = AfterImage.objects.get(name=AFTER_FILE_NAME).img
    after_img_url = after_img.url 

    base_dir = settings.IMG_ROOT
    file_name = after_img_url.split('/')[-1]
    to_save = os.path.join(base_dir, file_name)

    THRESHOLD = 150
    im = Image.open(before_img).convert('L')
    im_threshold = create_bit_image(im, THRESHOLD)
    f = open(to_save,'w')
    im_threshold.save(f, format='JPEG')
    im.close()
    im_threshold.close()
    f.close()

    THRESHOLD_FILE_NAME_START = 'threshold-'
    out_files = AfterImage.objects.filter(name__startswith='threshold-')
    out_file_urls = [im_obj.img.url for im_obj in out_files]
    logger.debug('Number of ursl: ' + str(len(out_file_urls)))
    # for i in range(256):
    #     name = THRESHOLD_FILE_NAME_START + str(i)
    #     im = Image.open(before_img).convert('L')
    #     im_threshold = create_bit_image(im, i)
    #     to_save = os.path.join(base_dir, name + '.jpg')
    #     im_temp = BytesIO()
    #     im_threshold.save(im_temp, 'JPEG')
    #     im_temp.seek(0)
    #     file_object = ContentFile(im_temp.read(), name + '.jpg')

    #     im_to_save = AfterImage(name=name, img=file_object)
    #     im_to_save.save()

    #     im.close()
    
    return render(request, 'BWSvg/home.html', {'before_img_url': before_img_url, 'out_file_urls': out_file_urls})

#def upload(request):
# need to take a post request of 
# file upload, then run the home
# function with this new uploaded file

#def download(request):
# reverse the image held in the current threshol
# 