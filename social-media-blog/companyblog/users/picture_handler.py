import os
from PIL import Image
from flask import url_for,current_app


def add_profile_pic(pic_upload,username):
    filename = pic_upload.filename
    #this lets you know what the file extension is jpg, png or something else
    ext_type = filename.split('.')[-1]
    #this saves the image as the username.jpg
    storage_filename  = str(usrname)+'.'+ext_type

    #get the root path of the app,
    #then look for static profile pics
    filepath = os.path.join(current_app.root_path,'static\profile_pics',storage_filename)

    output_size = (200,200)
    pic = Image.open(pic_upload)
    #thumbnail() resizes the image
    pic.thumbnail(output_size)
    pic.save(filepath)
    return storage_filename
