#!/usr/bin/env bash
if pip3 list | grep -F pyinstaller 2>&1 >/dev/null; echo $?;
    then
        echo "Pyinstaller is already installed";
    else
        pip3 install pyinstaller;
fi

pyinstaller src/addition.py --specpath spec --onefile
pyinstaller src/subtraction.py --specpath spec --onefile
pyinstaller src/square.py --specpath spec --onefile
pyinstaller src/complement.py --specpath spec --onefile
pyinstaller src/multiply.py --specpath spec --onefile

cp -r dist ~/.maths_test_tools
export PATH=$PATH:~/.maths_test_tools
echo -e "export PATH=$PATH:~/.maths_test_tools" >> ~/.bashrc
