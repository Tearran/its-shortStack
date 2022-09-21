# its_shorstack
its_shorstack is companion to display output from [its-i2cDevices](https://github.com/Tearran/its-i2cDevices)  for the Raspberry pi 
copy any its from [its-i2cDevices](https://github.com/Tearran/its-i2cDevices) to root of its-shortStack folder to see link
Change the permitions to 'chmod +x its-<name>.py to view on page

## Requirements 
- Debian arm-based distro
  - Rasberry pi (LST)(BUSTER) 
- python3
  - libraries include built-in

## Featured Scripts

- its_database.py 
  - sqlite3.db ~ A list of i2c [LKARS](https://www.lkars.com/) tested devices 

- its_pyWebApp - web app example 
  - Launches a simple web server
  - list files with the .py extension
  - exicutes .py and displays results on a web page
  - displays list on localhost:8000

### its scripts
basic use:
  python3 its_{name}.py

## its_pyWebApp
  ```bash
  python3 its_pyWebApp
  ```
# The following uses a bmp280 
and https://raw.githubusercontent.com/Tearran/its-i2cDevices/main/its_bmp280.py

```bash
https://github.com/Tearran/its-shortStack.git
cd its-shortStack
wget https://raw.githubusercontent.com/Tearran/its-i2cDevices/main/its_bmp280.py
chmod +x its_bmp280.py
python3 ./its_pyWebApp
```
![alt text](https://cdn.discordapp.com/attachments/988863432650543194/1022234845402902579/unknown.png "Logo Title Text 1")
### Tools
- [sqliteonline](https://sqliteonline.com/) - Playground
- [codepen.io](https://codepen.io/Tearran) - Playground
