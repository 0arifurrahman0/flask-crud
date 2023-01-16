## Setup & Installtion

### Setup a virtual environment
Instal virtual environment and make a virtual envvironment(v_env)
```python
pip install virtualenv
python -m virtualenv v_env
```

Activate a powershell in v_env
```cmd
./v_env/Scripts/activate.ps1
```

If you facing any permission related issue to activate the v_env then open <span style="color:yellow"> Windows PowerShell as Adminstrator </span> and give permissions.

```cmd
Set-ExecutionPolicy unrestricted 
```
### Install Dependencies
```cmd
pip install -r requirements.txt
```
### Run the application
```cmd
python main.py
```