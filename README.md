# CTS created by Brandon Hancock and Fiona Stockton December 7th 2017
Installation setup: These are the steps that you only run once when you are initally setting up the program.
cd ~/
git clone https://github.com/Brandon9598/CTS.github
python3 -m venv CTS_env
source CTS_env/bin/activate
pip install django==1.11.3
pip install Pillow
pip install Faker
cd CTS
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
"Username" <= insert your choice of username
"Enter email" <= insert your email of choice
"Password" <= insert your passwrod of choice
"Passwrod (again)" <= reenter same password
python manage.py runserver

Webiste setup: These are the steps that you have to do to set the webstie.
Go to 127.0.0.1:8000 in a web browser
Login if you have not done so already
Go to 127.0.0.1:8000 admin
Select the "Add" button next to "Groups"
Choose whatever name you want for the group. Example name would be "Staff"
Click the "Home" button on the left
Click the "Add" button next to "Users"
For each staff member, provide them with a unique username and password (can add in other personal information
if needed)
After each staff member, press save in the bottom right hand corner

Encryption and Decryption Process Setup:
Take decrpytOnBoot.sh, encryptOnShutdown.sh, runserver.sh out of the main CTS file and move to desktop.
cd ~/Desktop
sudo chmod +x decryptOnBoot.sh
sudo chmod +x encryptOnShutdown.sh
sudo chmod +x runserver.sh

***RUN EVERYTIME COMPUTER BOOTS***
double clip decryptOnBoot.sh and press "Exectue in Terminal"
Enter passphrase twice
double click runserver.sh and press "Exectue in Terminal"

***RUN EVERYTIME COMPUTER SHUTS DOWN***
double clip encryptOnShutdown.sh and press "Exectue in Terminal"
