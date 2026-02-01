# Win10

## Get powershell history
(Get-PSReadlineOption).HistorySavePath

## cli before session when open PS

## 
For Windows PowerShell, there's a similar concept to the .bashrc file in Linux called "PowerShell Profile". A PowerShell profile is a script that runs when PowerShell starts. You can use the profile as a logon script to customize the environment. You need to add your own commands to this script and every time you open a new PowerShell window, these commands will be executed.

Here's how you can set it up:

First, open PowerShell and check if a profile already exists with this command:
```
$profile
```
If it returns True, then you already have a profile. If it returns False, then you need to create one.

To create a profile, use the following command:
```
New-Item -path $profile -type file -force
```
After creating the profile, you can add your commands to it. Use the Notepad command to open your profile in notepad:
```
notepad.exe $profile
```

```
<path of miniconda3>\shell\condabin\conda-hook.ps1
conda activate py310
```

In the opened Notepad, you can write your own commands that you want to be executed whenever you start a new PowerShell session.

Save and close the file when you are finished editing.
Next time you open a new PowerShell window, your defined commands will be run.

Please note that due to security settings in some systems, scripts are not allowed to run by default. You might have to change the execution policy to make it work. You can do this by running this command in PowerShell with administrative privileges:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
This sets the policy for the current user to allow scripts that are written on the local computer and not downloaded from the internet. Be aware that changing the execution policy might expose you to the risk of running malicious scripts.