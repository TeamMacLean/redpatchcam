from tkinter.filedialog import askopenfilename, asksaveasfilename
from redpatchcam import buttons, options,sliders
import redpatch as rp


def set_thresholds(tab, seg, vals):
    v1, v2 = vals
    if seg == 'h':
        s1, s2 = 'H min', 'H max'
    elif seg == 's':
        s1, s2 = 'S min', 'S max'
    else:
        s1, s2 = 'V min', 'V max'
    sliders.thresholds[tab][s1].set(v1)
    sliders.thresholds[tab][s2].set(v2)
    sliders.tab_labels[tab][s1]['text'] = round(v1, 3)
    sliders.tab_labels[tab][s2]['text'] = round(v2, 3)

def import_settings():
    fs = rp.FilterSettings()
    fs.read(askopenfilename())
    for j in ['Scale Card', 'Leaf Area', 'Lesion Area']:
        for i in ('h','s','v'):
            set_thresholds(j, i, fs['leaf_area'][i])
            set_thresholds(j, i, fs['lesion_area'][i])
            set_thresholds(j, i, fs['scale_card'][i])
    for o in ['min_lesion_area', 'max_lc_ratio', 'min_lc_size', 'lc_prop_across_parent']:
        options.optvals[o].set(fs[o])



def export_settings(outfile=False):
    fs = buttons.make_fs()
    fs.settings['min_lesion_area'] = options.optvals['min_lesion_area'].get()
    fs.settings['max_lc_ratio'] = options.optvals['max_lc_ratio'].get()
    fs.settings['min_lc_size'] = options.optvals['min_lc_size'].get()
    fs.settings['lc_prop_across_parent'] = options.optvals['lc_prop_across_parent'].get()
    if outfile:
        fs.write(outfile)
    else:
        fs.write(asksaveasfilename(initialfile="filter_settings.yml"))