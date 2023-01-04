# install python compiler
pip install pyinstaller

# compile python code
pyinstaller -F password-gen.py

# copy executable to /user/bin
sudo cp ./dist/password-gen /usr/bin