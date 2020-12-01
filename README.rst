redpatchcam
===

A GUI app for running redpatch on Raspberry Pi with camera module

Prerequisites
=============

Relies on a Raspberry Pi version of `redpatch` on the `rasppi` branch at this repo:

https://github.com/TeamMacLean/redpatch/blob/rasppi/README.rst

Install that first, use the created `rpcam` conda env
Needs the ``picamera`` package ``pip install picamera``


Installation
============

``git clone https://github.com/TeamMacLean/redpatchcam.git``
``cd redpatchcam``
``pip install -e``

Start the app
=============

``python scripts/app.py`` 
