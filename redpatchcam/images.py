from PIL import Image, ImageTk
import redpatch as rp





rgb_subject = Image.open("default.jpg")
rgb_subject.thumbnail((400,400), Image.ANTIALIAS)
#rgb_subject.save('preview.gif', "GIF")
rgb_subject = rgb_subject.convert(mode="RGBA")
preview = ImageTk.PhotoImage(rgb_subject)

hsv_subject = rp.load_as_hsv("default.jpg")



image_panes = {}