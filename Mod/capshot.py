#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageGrab  # pip install pillow
from VideoCapture import Device

def get_shot(pic_name):
	pic=ImageGrab.grab()
	pic.save(pic_name)
	
def get_cam(pic_name):
	cam = Device()
	cam.saveSnapshot('image.jpg',quality=100,timestamp=3, boldfont=1)
	
def get_video():
	pass