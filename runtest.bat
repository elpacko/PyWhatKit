@REM set PYTHONPATH=.\pywhatskit
taskkill /im chromedriver.exe /f
python test_sendmessage.py

rem python -m IPython