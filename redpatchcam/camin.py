
import picamera
from io import BytesIO
import time
from PIL import Image, ImageTk
from redpatchcam import images

cbs = {}

def new_preview_cam():
    return picamera.PiCamera(resolution=(1600,1600))

preview_cam = new_preview_cam()

def get_stream():
        preview_cam.capture('fs.jpg')
        live_image = Image.open('fs.jpg')
        live_image.thumbnail((400,400), Image.ANTIALIAS)
        live_p = ImageTk.PhotoImage(live_image)
        images.image_panes['Preview'].config(image=live_p)
        images.image_panes['Preview'].image = live_p
        cbs['cam_update'] = images.image_panes['Preview'].after(100, lambda: get_stream() )

