from cx_Freeze import setup, Executable

includes=["re", "pyHook",'pythoncom','win32com','win32api','keywords','actions']

exe = Executable(
script="main.py",
base="console",
targetName = "CabalFAVENTO.exe",
icon="icon.ico"
)

setup(
name = "CabalFAVENTO",
version = "0.1",
description = "Cabal Event Bot - 720p",
options = {"build_exe": {"includes":includes}},
executables = [exe]
)