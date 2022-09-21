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
## its_database.py
  ```bash
  python3 its_database.py
  ```
## its_pyWebApp
  ```bash
  python3 its_pyWebApp
  ```

### Tools
- [sqliteonline](https://sqliteonline.com/) - Playground
- [codepen.io](https://codepen.io/Tearran) - Playground
