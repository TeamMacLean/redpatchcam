from PIL import Image, ImageTk
import redpatch as rp

rgb_subject = Image.open("/Users/macleand/Desktop/server_test/centered_leaf.jpg")
rgb_subject.thumbnail((400,400), Image.ANTIALIAS)
rgb_subject.save('preview.gif', "GIF")
rgb_subject = rgb_subject.convert(mode="RGBA")

preview = ImageTk.PhotoImage(rgb_subject)
hsv_subject = rp.load_as_hsv('preview.gif')

spinner = ImageTk.PhotoImage(Image.open("spinner.gif"))


image_panes = {}