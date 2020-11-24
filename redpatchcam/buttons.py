from redpatchcam import sliders, images, options
from tkinter import ttk
from tkinter.filedialog import askdirectory
import redpatch as rp
import numpy as np
from PIL import Image, ImageTk
from skimage import draw


def make_fs():
    fs = rp.FilterSettings()
    fs.add_setting('leaf_area', 
                   h=get_thresholds('Leaf Area', 'h'),
                   s=get_thresholds('Leaf Area', 's'),
                   v=get_thresholds('Leaf Area', 'v')
                      
    )
    fs.add_setting('healthy_area',
                   h=get_thresholds('Healthy Area', 'h'),
                   s=get_thresholds('Healthy Area', 's'),
                   v=get_thresholds('Healthy Area', 'v')
                   )
    fs.add_setting('lesion_area',
                   h=get_thresholds('Lesion Area', 'h'),
                   s=get_thresholds('Lesion Area', 's'),
                   v=get_thresholds('Lesion Area', 'v')
                   )
    fs.add_setting('lesion_centre',
                   h=get_thresholds('Lesion Centres', 'h'),
                   s=get_thresholds('Lesion Centres', 's'),
                   v=get_thresholds('Lesion Centres', 'v')
                   )
    fs.add_setting('scale_card',
                   h=get_thresholds('Scale Card', 'h'),
                   s=get_thresholds('Scale Card', 's'),
                   v=get_thresholds('Scale Card', 'v')
                   )
    return fs

def apply_button(parent, func):
    apply = ttk.Button(parent, command = func, text="Apply")
    return apply


def outputdir_button(parent):
    return ttk.Button(parent, command = get_output_dir, text='Choose' )

def get_output_dir():
    od = askdirectory()
    options.optvals['output_dir'].set(od)
    options.opts['output_dir']['text'] = od

def make_overlay(mask, alpha=0.5):
    alpha = int(255 * alpha)
    mask = mask.astype(np.uint8)
    leaf_area_array = np.dstack( (mask*128, mask*128, np.zeros_like(mask, dtype=np.uint8), np.zeros_like(mask,dtype=np.uint8)+alpha ) )
    mBlack = (leaf_area_array[:, :, 0:3] == [0, 0, 0]).all(2)
    leaf_area_array[mBlack] = (0,0,0,0)
    leaf_area_img = Image.fromarray(leaf_area_array, mode="RGBA")
    overlay = Image.alpha_composite(images.rgb_subject, leaf_area_img)
    return ImageTk.PhotoImage(overlay)

def get_thresholds(tab, seg):
    if seg == 'h':
        s1, s2 = 'H min', 'H max'
    elif seg == 's':
        s1, s2 = 'S min', 'S max'
    else:
        s1, s2 = 'V min', 'V max'
    return (sliders.thresholds[tab][s1].get(), sliders.thresholds[tab][s2].get() )

def do_overlay_leaf_area():
    h = get_thresholds('Leaf Area', 'h')
    s = get_thresholds('Leaf Area', 's')
    v = get_thresholds('Leaf Area', 'v')
    mask = rp.griffin_leaf_regions(images.hsv_subject, h=h, s=s, v=v)
    i = make_overlay(mask)
    #print(img_panes)
    images.image_panes['Leaf Area'].configure(image = i)
    images.image_panes['Leaf Area'].image = i
    #img_panes['Leaf Area'].configure(image = i)
    #img_panes['Leaf Area'].image = i
    
def do_overlay_healthy_area():
    h = get_thresholds('Healthy Area', 'h')
    s = get_thresholds('Healthy Area', 's')
    v = get_thresholds('Healthy Area', 'v')
    mask, _ = rp.griffin_healthy_regions(images.hsv_subject, h=h, s=s, v=v)
    i = make_overlay(mask)
    #pane.configure(image = i)
    #pane.image = i
    images.image_panes['Healthy Area'].configure(image = i)
    images.image_panes['Healthy Area'].image = i
    
def do_overlay_lesion_area():
    h = get_thresholds('Lesion Area', 'h')
    s = get_thresholds('Lesion Area', 's')
    v = get_thresholds('Lesion Area', 'v')
    mask, _ = rp.griffin_lesion_regions(images.hsv_subject, h=h, s=s, v=v)
    i = make_overlay(mask)
    #pane.configure(image = i)
    #pane.image = i
    images.image_panes['Lesion Area'].configure(image = i)
    images.image_panes['Lesion Area'].image = i

def do_overlay_lesion_centres():
    fs = make_fs()
    side_length = options.opts['side_length'].get()
    try:
        side_length = float(side_length)
    except ValueError:
        side_length = float('nan')
    scale = rp.griffin_scale_card(images.hsv_subject, h=fs['scale_card']['h'], s=fs['scale_card']['s'], v=fs['scale_card']['v'], side_length=side_length )

    if scale is None:
        scale = float('nan')
    pixel_length = 1/scale


    s = rp.SubImage(images.hsv_subject,1,'empty',file_settings=fs, dest_folder="none",
                    scale = scale,
                    pixel_length=pixel_length,
                    min_lesion_area=float(options.optvals['min_lesion_area'].get()),
                    max_lc_ratio=float(options.optvals['max_lc_ratio'].get()),
                    min_lc_size=float(options.optvals['min_lc_size'].get()),
                    lc_prop_across_parent=float(options.optvals['lc_prop_across_parent'].get())

                    )
    mask = np.zeros((400,400), dtype=np.uint8)
    for lc in s.lesion_centre_props:
        if lc.passed:
            ri, ci = draw.circle_perimeter(int(lc.corrected_centroid[0]), int(lc.corrected_centroid[1]), radius=5, shape=mask.shape)
            ro, co = draw.circle_perimeter(int(lc.corrected_centroid[0]), int(lc.corrected_centroid[1]), radius=8, shape=mask.shape)
            mask[ro,co] = 255
            mask[ri,ci] = 0
    i = make_overlay(mask, alpha=1)
    images.image_panes['Lesion Centres'].configure(image = i)
    images.image_panes['Lesion Centres'].image = i
    
def do_overlay_scale_card():
    h = get_thresholds('Scale Card', 'h')
    s = get_thresholds('Scale Card', 's')
    v = get_thresholds('Scale Card', 'v')
    mask = rp.griffin_leaf_regions(images.hsv_subject, h=h, s=s, v=v)
    i = make_overlay(mask)
    #pane.configure(image = i)
    #pane.image = i
    images.image_panes['Scale Card'].configure(image = i)
    images.image_panes['Scale Card'].image = i


apply_functions = {
    'Leaf Area': do_overlay_leaf_area,
    'Healthy Area': do_overlay_healthy_area,
    'Lesion Area': do_overlay_lesion_area,
    'Lesion Centres': do_overlay_lesion_centres,
    'Scale Card': do_overlay_scale_card
}
