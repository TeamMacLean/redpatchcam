
import tkinter as tk
opts = {}

optvals = {
    'min_lesion_area': tk.StringVar(value=1),
    'max_lc_ratio': tk.StringVar(value=2),
    'min_lc_size': tk.StringVar(value=2),
    'lc_prop_across_parent': tk.StringVar(value=0.2),
    'output_dir': tk.StringVar(value="None Selected")
}