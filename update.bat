@echo off
echo Enter your commit message:
set /p commitMsg=
git add .
git commit -m "%commitMsg%"
git push
