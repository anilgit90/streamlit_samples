@echo off
REM Change the following variables to match your repository details
SET REMOTE_REPO_URL=https://github.com/anilgit90/streamlit_samples.git
SET BRANCH_NAME=main

REM Check if the current directory is a Git repository
git rev-parse --is-inside-work-tree > nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo This directory is not a Git repository. Initialize Git first.
    exit /b
)

REM Add your changes to the staging area
git add .

REM Prompt for a commit message
set /p COMMIT_MESSAGE="Enter your commit message: "

REM Commit your changes
git commit -m "%COMMIT_MESSAGE%"

REM Push to the remote repository
git push %REMOTE_REPO_URL% %BRANCH_NAME%

REM Optional: Check if the push was successful
IF %ERRORLEVEL% EQU 0 (
    echo Push successful!
) ELSE (
    echo Error pushing changes. Check your configuration.
)