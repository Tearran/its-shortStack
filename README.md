# its_shorstack
is a python3 web server and app for the Raspberry pi 
Usage:
- i2c component testing
- Bash pipes
- SQL Data

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
  - list apps folder files with the .py extension
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
### Libraries
- [bmp280](https://github.com/Tearran/bmp280) - Weather Sensor
- [FaBo9AXIS-MPU9250-Python](https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python) - Inertial measurement sensor
- [Melopero_AMG8833](https://github.com/melopero/Melopero_AMG8833) - 8x8 ir camera ( aka grideye )
