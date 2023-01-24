### Setup Raspberry pi
1. https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/configure-your-pi
2. https://geektechstuff.com/2020/06/01/python-and-bluetooth-part-1-scanning-for-devices-and-services-python/
3. https://pimylifeup.com/upgrade-raspbian-stretch-to-raspbian-buster/
4. https://pimylifeup.com/upgrade-raspbian-stretch-to-raspbian-buster/
5. https://linuxize.com/post/how-to-install-python-3-9-on-debian-10/
6. https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3
7. https://ronm333.medium.com/virtual-environments-on-the-raspberry-pi-ead158a72cd5
8. https://raspberrypi.stackexchange.com/questions/99686/raspberry-pi-error-python-gui-no-display-name-and-no-display-environment-var
9. https://raspberrypi.stackexchange.com/questions/38294/error-when-attempting-to-create-python-gui-using-tkinter-no-display-name-and-n
10. https://stackoverflow.com/questions/40861638/python-tkinter-treeview-not-allowing-modal-window-with-direct-binding-like-on-ri

### Install pip and Bluetooth library
1. https://www.activestate.com/resources/quick-reads/how-to-install-pip-on-windows/
2. https://github.com/pybluez/pybluez/blob/master/docs/install.rst
3. https://github.com/pybluez/pybluez/issues/431
4. https://github.com/pybluez/pybluez/issues/236
5. pip install pybluez2 (for windows)

### Issues with pybluez library
````shell
sudo apt-get update
sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
pip3 install Cmake
sudo apt-get install libbluetooth-dev
pip3 install git+https://github.com/pybluez/pybluez.git#egg=pybluez
````

### Fix UTF-8 database issue
1. https://stackoverflow.com/questions/73244027/character-set-utf8-unsupported-in-python-mysql-connector

### Libraries
1. pip3 install mysql-connector-python==8.0.29
2. pip3 install pybluez
3. pip3 install pyyaml
4. pip3 install SpeechRecognition
5. pip3 install customtkinter
6. pip3 install python-dotenv
7. pip3 install Pillow

### Connect to PIs in local network via ssh
````shell
ssh pi@raspberry.local
ssh pi@vipperpi.local
````