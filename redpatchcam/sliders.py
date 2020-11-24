from tkinter import ttk
import tkinter as tk
from collections import defaultdict
import redpatch as rp

tab_labels = defaultdict(dict)
tab_slider = defaultdict(dict)


app = tk.Tk()
app.geometry("800x480")
app.title("redpatchcam")



def make_thresholds():
    return {
     'Leaf Area': {
         'H min': tk.DoubleVar(value=rp.LEAF_AREA_HUE[0]),
         'H max': tk.DoubleVar(value=rp.LEAF_AREA_HUE[1]),
         'S min': tk.DoubleVar(value=rp.LEAF_AREA_SAT[0]),
         'S max': tk.DoubleVar(value=rp.LEAF_AREA_SAT[1]),
         'V min': tk.DoubleVar(value=rp.LEAF_AREA_VAL[0]),
         'V max': tk.DoubleVar(value=rp.LEAF_AREA_VAL[1])
     },
     'Healthy Area': {
         'H min': tk.DoubleVar(value=rp.HEALTHY_HUE[0]),
         'H max': tk.DoubleVar(value=rp.HEALTHY_HUE[1]),
         'S min': tk.DoubleVar(value=rp.HEALTHY_SAT[0]),
         'S max': tk.DoubleVar(value=rp.HEALTHY_SAT[1]),
         'V min': tk.DoubleVar(value=rp.HEALTHY_VAL[0]),
         'V max': tk.DoubleVar(value=rp.HEALTHY_VAL[1])
     },
     'Lesion Area': {
         'H min': tk.DoubleVar(value=rp.LESION_HUE[0]),
         'H max': tk.DoubleVar(value=rp.LESION_HUE[1]),
         'S min': tk.DoubleVar(value=rp.LESION_SAT[0]),
         'S max': tk.DoubleVar(value=rp.LESION_SAT[1]),
         'V min': tk.DoubleVar(value=rp.LESION_VAL[0]),
         'V max': tk.DoubleVar(value=rp.LESION_VAL[1])
     },
     'Lesion Centres': {
         'H min': tk.DoubleVar(value=rp.LESION_CENTRE_HUE[0]),
         'H max': tk.DoubleVar(value=rp.LESION_CENTRE_HUE[1]),
         'S min': tk.DoubleVar(value=rp.LESION_CENTRE_SAT[0]),
         'S max': tk.DoubleVar(value=rp.LESION_CENTRE_SAT[1]),
         'V min': tk.DoubleVar(value=rp.LESION_CENTRE_VAL[0]),
         'V max': tk.DoubleVar(value=rp.LESION_CENTRE_VAL[1])
     },
     'Scale Card': {
         'H min': tk.DoubleVar(value=rp.SCALE_CARD_HUE[0]),
         'H max': tk.DoubleVar(value=rp.SCALE_CARD_HUE[1]),
         'S min': tk.DoubleVar(value=rp.SCALE_CARD_SAT[0]),
         'S max': tk.DoubleVar(value=rp.SCALE_CARD_SAT[1]),
         'V min': tk.DoubleVar(value=rp.SCALE_CARD_VAL[0]),
         'V max': tk.DoubleVar(value=rp.SCALE_CARD_VAL[1])
     }
 }

thresholds = make_thresholds()

def default_slider(parent,var,func):
    slider = ttk.Scale(parent, from_=0.0, to=1.0, length=200, variable=var, command=func)
    return slider

########### Leaf Area Slider Functions ######################
def la_h_min_update(var):
    var = float(var)
    tab_labels['Leaf Area']['H min']['text'] = round(var,3)
    if var > thresholds['Leaf Area']['H max'].get():
        tab_slider['Leaf Area']['H max'].set(var)
        tab_labels['Leaf Area']['H max']['text'] = round(var,3)

def la_h_max_update(var):
    var = float(var)
    tab_labels['Leaf Area']['H max']['text'] = round(var,3)
    if var < thresholds['Leaf Area']['H min'].get():
        tab_slider['Leaf Area']['H min'].set(var)
        tab_labels['Leaf Area']['H min']['text'] = round(var,3)

def la_s_min_update(var):
    var = float(var)
    tab_labels['Leaf Area']['S min']['text'] = round(var,3)
    if var > thresholds['Leaf Area']['S max'].get():
        tab_slider['Leaf Area']['S max'].set(var)
        tab_labels['Leaf Area']['S max']['text'] = round(var,3)

def la_s_max_update(var):
    var = float(var)
    tab_labels['Leaf Area']['S max']['text'] = round(var,3)
    if var < thresholds['Leaf Area']['S min'].get():
        tab_slider['Leaf Area']['S min'].set(var)
        tab_labels['Leaf Area']['S min']['text'] = round(var,3)

def la_v_min_update(var):
    var = float(var)
    tab_labels['Leaf Area']['V min']['text'] = round(var,3)
    if var > thresholds['Leaf Area']['V max'].get():
        tab_slider['Leaf Area']['V max'].set(var)
        tab_labels['Leaf Area']['V max']['text'] = round(var,3)

def la_v_max_update(var):
    var = float(var)
    tab_labels['Leaf Area']['V max']['text'] = round(var,3)
    if var < thresholds['Leaf Area']['V min'].get():
        tab_slider['Leaf Area']['V min'].set(var)
        tab_labels['Leaf Area']['V min']['text'] = round(var,3)

########### Healthy Area Slider Functions ######################
def ha_h_min_update(var):
    var = float(var)
    tab_labels['Healthy Area']['H min']['text'] = round(var,3)
    if var > thresholds['Healthy Area']['H max'].get():
        tab_slider['Healthy Area']['H max'].set(var)
        tab_labels['Healthy Area']['H max']['text'] = round(var,3)


def ha_h_max_update(var):
    var = float(var)
    tab_labels['Healthy Area']['H max']['text'] = round(var,3)
    if var < thresholds['Healthy Area']['H min'].get():
        tab_slider['Healthy Area']['H min'].set(var)
        tab_labels['Healthy Area']['H min']['text'] = round(var,3)


def ha_s_min_update(var):
    var = float(var)
    tab_labels['Healthy Area']['S min']['text'] = round(var,3)
    if var > thresholds['Healthy Area']['S max'].get():
        tab_slider['Healthy Area']['S max'].set(var)
        tab_labels['Healthy Area']['S max']['text'] = round(var,3)


def ha_s_max_update(var):
    var = float(var)
    tab_labels['Healthy Area']['S max']['text'] = round(var,3)
    if var < thresholds['Healthy Area']['S min'].get():
        tab_slider['Healthy Area']['S min'].set(var)
        tab_labels['Healthy Area']['S min']['text'] = round(var,3)


def ha_v_min_update(var):
    var = float(var)
    tab_labels['Healthy Area']['V min']['text'] = round(var,3)
    if var > thresholds['Healthy Area']['V max'].get():
        tab_slider['Healthy Area']['V max'].set(var)
        tab_labels['Healthy Area']['V max']['text'] = round(var,3)


def ha_v_max_update(var):
    var = float(var)
    tab_labels['Healthy Area']['V max']['text'] = round(var,3)
    if var < thresholds['Healthy Area']['V min'].get():
        tab_slider['Healthy Area']['V min'].set(var)
        tab_labels['Healthy Area']['V min']['text'] = round(var,3)

########### Lesion Area Slider Functions ######################
def lea_h_min_update(var):
    var = float(var)
    tab_labels['Lesion Area']['H min']['text'] = round(var,3)
    if var > thresholds['Lesion Area']['H max'].get():
        tab_slider['Lesion Area']['H max'].set(var)
        tab_labels['Lesion Area']['H max']['text'] = round(var,3)


def lea_h_max_update(var):
    var = float(var)
    tab_labels['Lesion Area']['H max']['text'] = round(var,3)
    if var < thresholds['Lesion Area']['H min'].get():
        tab_slider['Lesion Area']['H min'].set(var)
        tab_labels['Lesion Area']['H min']['text'] = round(var,3)


def lea_s_min_update(var):
    var = float(var)
    tab_labels['Lesion Area']['S min']['text'] = round(var,3)
    if var > thresholds['Lesion Area']['S max'].get():
        tab_slider['Lesion Area']['S max'].set(var)
        tab_labels['Lesion Area']['S max']['text'] = round(var,3)


def lea_s_max_update(var):
    var = float(var)
    tab_labels['Lesion Area']['S max']['text'] = round(var,3)
    if var < thresholds['Lesion Area']['S min'].get():
        tab_slider['Lesion Area']['S min'].set(var)
        tab_labels['Lesion Area']['S min']['text'] = round(var,3)


def lea_v_min_update(var):
    var = float(var)
    tab_labels['Lesion Area']['V min']['text'] = round(var,3)
    if var > thresholds['Lesion Area']['V max'].get():
        tab_slider['Lesion Area']['V max'].set(var)
        tab_labels['Lesion Area']['V max']['text'] = round(var,3)


def lea_v_max_update(var):
    var = float(var)
    tab_labels['Lesion Area']['V max']['text'] = round(var,3)
    if var < thresholds['Lesion Area']['V min'].get():
        tab_slider['Lesion Area']['V min'].set(var)
        tab_labels['Lesion Area']['V min']['text'] = round(var,3)

########## Lesion Centre Slider Functions ######################
def lec_h_min_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['H min']['text'] = round(var,3)
    if var > thresholds['Lesion Centres']['H max'].get():
        tab_slider['Lesion Centres']['H max'].set(var)
        tab_labels['Lesion Centres']['H max']['text'] = round(var,3)


def lec_h_max_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['H max']['text'] = round(var,3)
    if var < thresholds['Lesion Centres']['H min'].get():
        tab_slider['Lesion Centres']['H min'].set(var)
        tab_labels['Lesion Centres']['H min']['text'] = round(var,3)


def lec_s_min_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['S min']['text'] = round(var,3)
    if var > thresholds['Lesion Centres']['S max'].get():
        tab_slider['Lesion Centres']['S max'].set(var)
        tab_labels['Lesion Centres']['S max']['text'] = round(var,3)


def lec_s_max_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['S max']['text'] = round(var,3)
    if var < thresholds['Lesion Centres']['S min'].get():
        tab_slider['Lesion Centres']['S min'].set(var)
        tab_labels['Lesion Centres']['S min']['text'] = round(var,3)


def lec_v_min_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['V min']['text'] = round(var,3)
    if var > thresholds['Lesion Centres']['V max'].get():
        tab_slider['Lesion Centres']['V max'].set(var)
        tab_labels['Lesion Centres']['V max']['text'] = round(var,3)


def lec_v_max_update(var):
    var = float(var)
    tab_labels['Lesion Centres']['V max']['text'] = round(var,3)
    if var < thresholds['Lesion Centres']['V min'].get():
        tab_slider['Lesion Centres']['V min'].set(var)
        tab_labels['Lesion Centres']['V min']['text'] = round(var,3)
        
########## Scale Card Slider Functions ######################

def sc_h_min_update(var):
    var = float(var)
    tab_labels['Scale Card']['H min']['text'] = round(var,3)
    if var > thresholds['Scale Card']['H max'].get():
        tab_slider['Scale Card']['H max'].set(var)
        tab_labels['Scale Card']['H max']['text'] = round(var,3)


def sc_h_max_update(var):
    var = float(var)
    tab_labels['Scale Card']['H max']['text'] = round(var,3)
    if var < thresholds['Scale Card']['H min'].get():
        tab_slider['Scale Card']['H min'].set(var)
        tab_labels['Scale Card']['H min']['text'] = round(var,3)


def sc_s_min_update(var):
    var = float(var)
    tab_labels['Scale Card']['S min']['text'] = round(var,3)
    if var > thresholds['Scale Card']['S max'].get():
        tab_slider['Scale Card']['S max'].set(var)
        tab_labels['Scale Card']['S max']['text'] = round(var,3)


def sc_s_max_update(var):
    var = float(var)
    tab_labels['Scale Card']['S max']['text'] = round(var,3)
    if var < thresholds['Scale Card']['S min'].get():
        tab_slider['Scale Card']['S min'].set(var)
        tab_labels['Scale Card']['S min']['text'] = round(var,3)


def sc_v_min_update(var):
    var = float(var)
    tab_labels['Scale Card']['V min']['text'] = round(var,3)
    if var > thresholds['Scale Card']['V max'].get():
        tab_slider['Scale Card']['V max'].set(var)
        tab_labels['Scale Card']['V max']['text'] = round(var,3)


def sc_v_max_update(var):
    var = float(var)
    tab_labels['Scale Card']['V max']['text'] = round(var,3)
    if var < thresholds['Scale Card']['V min'].get():
        tab_slider['Scale Card']['V min'].set(var)
        tab_labels['Scale Card']['V min']['text'] = round(var,3)

functions = {
'Leaf Area': {
        'H min': la_h_min_update,
        'H max': la_h_max_update,
        'S min': la_s_min_update,
        'S max': la_s_max_update,
        'V min': la_v_min_update,
        'V max': la_v_max_update,
    },
'Healthy Area': {
        'H min': ha_h_min_update,
        'H max': ha_h_max_update,
        'S min': ha_s_min_update,
        'S max': ha_s_max_update,
        'V min': ha_v_min_update,
        'V max': ha_v_max_update,
    },
'Lesion Area': {
        'H min': lea_h_min_update,
        'H max': lea_h_max_update,
        'S min': lea_s_min_update,
        'S max': lea_s_max_update,
        'V min': lea_v_min_update,
        'V max': lea_v_max_update,
    },
'Lesion Centres': {
        'H min': lec_h_min_update,
        'H max': lec_h_max_update,
        'S min': lec_s_min_update,
        'S max': lec_s_max_update,
        'V min': lec_v_min_update,
        'V max': lec_v_max_update,
    },
'Scale Card': {
        'H min': sc_h_min_update,
        'H max': sc_h_max_update,
        'S min': sc_s_min_update,
        'S max': sc_s_max_update,
        'V min': sc_v_min_update,
        'V max': sc_v_max_update,
    },
}