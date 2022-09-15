# its-i2cDevices
its-i2cDevices is a collection of i2c device software for the Raspberry pi 
Useage:
- i2c component testing
- Bash pipe
- python3 webapps
- SSH Ploter
- sql Data

## Featured Scripts

- its_database.py 
  - sqlite3.db ~ A list of i2c [LKARS](https://www.lkars.com/) tested devices 
- its_bmp280.py - Temprature and barametric pressure 
- its_amg8833.py - 8x8 IR camera ( aka: GridEye )
- its_mlx90614.py -  infrared thermometer
- its_mpu60xx.py - 6-axis Inertial measurement unit 
- its_pyWebApp.py - web app example 
  - Launches a simple web server
  - list apps folder files with .py extention
  - displays list on localhost:8000

### its scripts
basic use:
  python3 its_{name}.py
## its_database.py
  ```bash
  python3 its_database.py
  ```
  ```bash
  python3 its_bmp280.py
  ```
  ```bash
  python3 its_pyWebApp.py
  ```
  etc..

### Tools and Resources
- [sqliteonline](https://sqliteonline.com/) - Playground
- [bmp280](https://github.com/Tearran/bmp280) - Sensor Driver
