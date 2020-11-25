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
    python_requires='>=3.6',
    install_requires=[
        "redpatch >= 0.2.2",
    ]
)