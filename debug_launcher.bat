@echo off
REM starts a Powershell with tail to monitor the debug.log file as the program runs.
echo Launching: Powershell and tailing 'debug.log'.
start cmd /c Powershell Get-Content -Path 'debug.log' -Wait

REM Runs all test files in scripts/test using python3
REM     ~consider moving this functionality to git push
for /r %%i in (scripts\tests\*) do (
    echo Executing Test: %%i
    python3 -B "%%i"
)
    
REM runs main.py using python3
echo Running: main.py.
python3 -B "%~dp0main.py" %*
pause