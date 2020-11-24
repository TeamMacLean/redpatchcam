from setuptools import setup

setup(
    name='redpatchcam',
    version='0.0.0',
    packages=['redpatchcam'],
    url='https://github.com/TeamMacLean/redpatchcam',
    license='LICENSE.txt',
    author='Dan MacLean',
    author_email='dan.maclean@tsl.ac.uk',
    description='redpatch instance on Pi Cam',
    scripts=['scripts/app.py'],
    python_requires='>=3.7',
    install_requires=[
        "guizero == 1.1.0",
        "pillow == 8.0.1",
        "tk == 8.6.10",
        "numpy == 1.19.4",
        "redpatch == 0.2.1",
        "scikit-image == 0.17.2"
    ]
)