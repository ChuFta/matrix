@echo off
mode 800
title Matrix
color A
cls

:beggining
cls
set /P c=Are you sure you want to continue, this might make your PC unstable [Y/N]?
if /I "%c%" EQU "Y" goto :end
if /I "%c%" EQU "N" goto :beggining

:end
cls
python matrix.py
PAUSE