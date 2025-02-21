# lkc_leap
Trying to get data from the leap motion 2 controller from Python using LeapC API

# installation

- Download and install the *Gemini* hand tracking software from ultraleap (products -> leap motion cont. 2 -> download button)  
- Make a work folder for your leap project (or move to a new repo local repo if you use github)    
- Download the leap python binding code .zip file from the repo at https://github.com/ultraleap/leapc-python-bindings  
- Move the downloaded .zip file to your work folder for your project and unzip it   

# Make a python virtual environment for v3.8
Open a terminal in your project folder (or `cd` to your project folder from home)  
For Conda (or Anaconda) users:  
`conda create --name leap python=3.8`  

# Activate the virtual environment 
`conda activate leap`  
(use `conda deactivate` to go back to your regular Python environment)

# Install the leapc stuff: 
`pip install -r requirements.txt`    
`pip install -e leapc-python-api`    

# Plug in your leap!!!
And then test the installation by running an example:  
`python examples/tracking_event_example.py`  
