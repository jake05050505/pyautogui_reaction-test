# Installation
This project uses a virtual environment due to the inclusion of a non-standard python libary (pyautogui) and its dependencies.
## To install:
### First, you need python installed.
You can skip this step if you have python installed (C:\Users\\<mark>yourname</mark>\AppData\Local\Programs\Python\Python313\) or (C:\Python313)  

Install the most recent download of Python at https://www.python.org/downloads/
Alternatively, you can use a package manager such as winget `winget install python`.

### Install pyautogui_reaction-test (<bold>First time only</bold>)
1. Clone the repository into a folder of choice.
2. If you haven't done so already, open a terminal in the same folder.
3. Run `python -m venv venv` to create a virtual environment named "venv".
4. Activate the virtual environment by using the venv activate script which corresponds to your shell:  
  Windows PowerShell:  
  `venv\Scripts\Activate.ps1`  
  Windows Command Prompt:  
  `venv\Scripts\activate.bat`  
5. Run `pip install -r requirements.txt`, this will install the project's dependencies into your virtual environment.
  The installation is now complete.
6. Now, run `python app.py`.

## After first install
After the first install, some steps become unnecessary.  
To run the app again, repeat steps 2, 4, and 6.
