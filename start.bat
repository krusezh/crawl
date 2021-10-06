@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
set CONDAPATH=D:\anaconda3
set ENVNAME=inception
if %ENVNAME%==base (set ENVPATH=%CONDAPATH%) else (set ENVPATH=%CONDAPATH%\envs\%ENVNAME%)
call %CONDAPATH%\Scripts\activate.bat %ENVPATH%
rem set path=D:\anaconda3\envs\inception
python --version
python D:\Documents\crawl\main.py
rem call conda deactivate
pause