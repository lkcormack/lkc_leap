# lkc_leap
Trying to get data from the leap motion 2 controller from Python using LeapC API

# installation

Install *Gemini* hand tracking software from ultraleap (products -> leap motion cont. 2 -> download button
Download code .zip from https://github.com/ultraleap/leapc-python-bindings
Make a work folder or repo folder
unzip python bindings in folder

# Make a python virtual environment for v3.8
e.g. conda create --name leap python=3.8
Activate venv

# Install the leapc stuff: 
pip install -r requirements.txt
pip install -e leapc-python-api

# Plug in your leap!!!
And then test the installation by running an example:
python examples/tracking_event_example.py
