@echo off
set task_time_minute=5
set task_name="gmail check"
set /A launch_dir:"%~dp0"
:set current_dir:"%CD%"
echo ACTIVATE task %task_name%...
schtasks /create /tn %task_name% /tr "%launch_dir%\gmail.exe" /sc minute /mo /V1 %task_time_minute%
:schtasks /create /tn %task_name% /tr "\"%launch_dir%\gmail.exe\"" /sc minute /mo %task_time_minute%

echo CHECKING task %task_name%...
schtasks /query /tn %task_name%
schtasks /query /tn %task_name% /v /fo list | find "Status:"
schtasks /ShowSid /TN %task_name%
:control schedtasks
taskschd.msc
pause