RMDIR /S /Q build
timeout 2
python setup.py build
copy build\exe.win32-2.7\library.zip  "C:\Users\Desk\Google Drive\Macro cabal\library.zip"
mkdir build\CabalFAVENTO
timeout 1
move build\exe.win32-2.7 build\CabalFAVENTO\bin
timeout 2
copy defaults\* build\CabalFAVENTO\
Robocopy defaults\ build\CabalFAVENTO\ /E
copy icone.ico  build\CabalFAVENTO\bin\CabalFAVENTO.ico
timeout 1
build\CabalFAVENTO\bin\CabalFAVENTO
