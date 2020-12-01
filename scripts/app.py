from redpatchcam import sliders, buttons, images, options, files, camin
from tkinter import ttk
import tkinter as tk
import tempfile
import subprocess
import shutil
import os
import logging
import datetime
import picamera
from io import BytesIO
import time
import redpatch as rp
from PIL import Image, ImageTk


app = sliders.app

tab_names = ['Scale Card','Leaf Area', 'Lesion Area', 'Lesion Centres']
slider_names = ['H min', 'H max', 'S min', 'S max', 'V min', 'V max']

menu = tk.Menu(app)
app.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Settings', menu=filemenu)
filemenu.add_command(label = 'Import', command=files.import_settings)
filemenu.add_command(label="Export", command=files.export_settings)


tabs = ttk.Notebook(app)

def make_bp(dir, filter_dir, start_time):
    cmd = ["redpatch-batch-process",
        "--use_on_server",
        "--source_folder", dir,
        "--destination_folder", os.path.join(options.optvals['output_dir'].get(),start_time ),
        "--filter_settings", os.path.join(filter_dir, "filter_settings.yml"),
        "--min_lesion_area", options.optvals['min_lesion_area'].get(),
        "--max_lc_ratio", options.optvals['max_lc_ratio'].get(),
        "--min_lc_size", options.optvals['min_lc_size'].get(),
        "--lc_prop_across_parent", options.optvals['lc_prop_across_parent'].get()
    ]
    side_length = options.opts['side_length'].get()
    if side_length:
        cmd = cmd + [
            "--scale_image_name", "redpatch_cam_image.jpg",
            "--scale_card_side_length", side_length
        ]

    return cmd

def run_batch():



    if options.optvals['output_dir'].get() == 'None Selected':
        result_label['text'] = "No Output Folder Selected. Please select before creating report"
        result_label.grid(column=0, row=6)
        return None

    progress = ttk.Progressbar(tab_store['Report'], length = 200, mode='determinate')
    progress.grid(column=0, row=5)

    progress['value'] = 20
    app.update()
    start_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    os.mkdir(os.path.join(options.optvals['output_dir'].get(), start_time))
    try:
        temp_dir = tempfile.TemporaryDirectory()
        filter_dir = tempfile.TemporaryDirectory(dir=temp_dir.name)
        logging.basicConfig(filename=os.path.join(options.optvals['output_dir'].get(), start_time, 'logfile.txt'), level=logging.DEBUG, filemode='w')
        shutil.copy("working_image.jpg", os.path.join(temp_dir.name, "redpatchcam_image.jpg") )
        files.export_settings(os.path.join(filter_dir.name, "filter_settings.yml"))
        command = make_bp(temp_dir.name, filter_dir.name,start_time)
        progress['value'] = 40
        app.update()
        logging.info(" ".join(command) )
        process = subprocess.run(command, stdout=subprocess.PIPE)
        if process.returncode == 0:
            logging.info("Completed Successfully")
            progress['value'] = 100
            app.update()
            result_label['text'] = "Done. Report saved to {}/{}".format(options.optvals['output_dir'].get(), start_time)
            result_label.grid(column=0, row=6)
        else:
            logging.error("ERROR IN batch-process subprocess")
            logging.error(process.stderr)
            result_label['text'] = "Something went wrong. Error log in {}/{}/logfile.txt".format(options.optvals['output_dir'].get(), start_time)
            result_label.grid(column=0, row=6)
    except Exception as e:
        logging.error("EXCEPTION in setup for batch-process subprocess")
        logging.error(str(e))
        result_label['text'] = "Something went wrong. Error Report dumped to {}/{}".format(options.optvals['output_dir'].get(), start_time)
        result_label.grid(column=0, row=6)
    finally:
        filter_dir.cleanup()
        temp_dir.cleanup()
        for f in ['fs.jpg', 'preview.jpg', 'working_image.jpg']:
            if os.path.exists(f):
                os.remove(f)




apply_buttons = {}
tab_store = {}

t = ttk.Frame(tabs)
tabs.add(t, text="Preview")
tab_store['Preview'] = t
images.image_panes['Preview'] = ttk.Label(t, image=images.preview)
images.image_panes['Preview'].grid(column=0, row=0, rowspan=15)


camin.get_stream()

def make_final_image():
    app.after_cancel(camin.cbs['cam_update'])
    buttons.preview_button['Preview'].destroy()
    camin.preview_cam.close()
    time.sleep(2)
    del camin.preview_cam

    shutil.copyfile('fs.jpg', 'working_image.jpg')
    fi = Image.open("fs.jpg")
    fi.thumbnail((400,400), Image.ANTIALIAS)
    fi = fi.convert(mode="RGBA")
    fi.save('preview.jpg', "JPEG")
    images.preview = ImageTk.PhotoImage(fi)
    images.hsv_subject = rp.load_as_hsv('preview.jpg')
    images.rgb_subject = fi
    for n in ['Scale Card','Leaf Area', 'Lesion Area', 'Lesion Centres']:
        images.image_panes[n].config(image=images.preview) 
        images.image_panes[n].image = images.preview


buttons.preview_button['Preview'] = ttk.Button(tab_store['Preview'], command = make_final_image, text = "Use this image")
buttons.preview_button['Preview'].grid(column=2, row=8, padx=20)

for n in tab_names:
    t = ttk.Frame(tabs)
    tabs.add(t, text=n)
    tab_store[n] = t
    for i, sn in enumerate(slider_names):
            if not n in 'Lesion Centres':
                ttk.Label(t, text=sn).grid(column=0, row=(i*2))
                sliders.tab_slider[n][sn] = sliders.default_slider(t, sliders.thresholds[n][sn], sliders.functions[n][sn]) #functions[n][sn] )
                sliders.tab_slider[n][sn].grid(column=1, row=(i*2))
                sliders.tab_labels[n][sn] = ttk.Label(t,text=str(round(sliders.thresholds[n][sn].get(),3) ) )
                sliders.tab_labels[n][sn].grid(column=2, row=(i*2))
    images.image_panes[n] = ttk.Label(t, image=images.preview)
    images.image_panes[n].grid(column=3, row=0, rowspan=15)
    apply_buttons[n] = buttons.apply_button(t, buttons.apply_functions[n]) #(images.hsv_subject, image_panes[n]) )
    apply_buttons[n].grid(column = 0, row = 11)

ttk.Label(tab_store['Scale Card'], text="Select Scale Card Side Length (cm).").grid(column=0,row=12, columnspan=3)
ttk.Label(tab_store['Scale Card'], text="(Leave Blank if no Scale Card)").grid(column=0,row=13, columnspan=3)

options.opts['side_length'] = ttk.Combobox(tab_store['Scale Card'], values= tuple([0.25 * i for i in range(1,60)]) )
options.opts['side_length'].grid(column = 1, row = 14)

ttk.Label(tab_store['Lesion Centres'], text="Min Lesion Area (cm2)").grid(column=0, row=2)
options.opts['min_lesion_area'] = ttk.Entry(tab_store['Lesion Centres'],textvariable=options.optvals['min_lesion_area'],width=5)
options.opts['min_lesion_area'].grid(column=1, row =2)


ttk.Label(tab_store['Lesion Centres'], text="Max Centre Length:Width").grid(column=0, row=3)
options.opts['max_lc_ratio'] = ttk.Entry(tab_store['Lesion Centres'], textvariable=options.optvals['max_lc_ratio'],width=5)
options.opts['max_lc_ratio'].grid(column=1, row =3)

ttk.Label(tab_store['Lesion Centres'], text="Min Centre Area (cm2)").grid(column=0, row=4)
options.opts['max_lc_ratio'] = ttk.Entry(tab_store['Lesion Centres'], textvariable=options.optvals['min_lc_size'],width=5)
options.opts['max_lc_ratio'].grid(column=1, row =4)

ttk.Label(tab_store['Lesion Centres'], text="Min Prop Across Lesion").grid(column=0, row=5)
options.opts['max_lc_ratio'] = ttk.Entry(tab_store['Lesion Centres'], textvariable=options.optvals['lc_prop_across_parent'],width=5)
options.opts['max_lc_ratio'].grid(column=1, row =5)

tab_store['Report'] = ttk.Frame(tabs)
tabs.add(tab_store['Report'], text='Report')


ttk.Label(tab_store['Report'], text="Report Output Folder").grid(column=0,row=1)
buttons.outputdir_button(tab_store['Report']).grid(column=0, row=2)
options.opts['output_dir'] = ttk.Label(tab_store['Report'], text=options.optvals['output_dir'].get())
options.opts['output_dir'].grid(column=0,row=3)

run_button = ttk.Button(tab_store['Report'], command = run_batch, text='Create Report')
run_button.grid(column=0, row=4, ipadx=50)

result_label = ttk.Label(tab_store['Report'], text="Nothing done yet: output_dir = {}".format(options.optvals['output_dir'].get()) )
result_label.grid_remove()




tabs.pack(expand=1, fill="both")




app.mainloop()
