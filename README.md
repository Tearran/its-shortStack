# its-i2cDevices
its-i2cDevices is a collection of i2c device software for the Raspberry pi 
Used as
- i2c component tester
- Bash pipe

## Featured Scripts

- its_database.py 
  - sqlite3.db ~ A list of i2c [LKARS](https://www.lkars.com/) tested devices 
- its_bmp280.py - Temprature and barametric pressure 

### its scripts
basic use:
  python3 its_{name}.py
## its_database.py
  ```bash
  python3 its_database.py
  ```
 ## its_bmp280.py
  ```bash
  python3 its_bmp280.py
  ```

### Tools and Resources
- [sqliteonline](https://sqliteonline.com/) - Playground
- [bmp280](https://github.com/Tearran/bmp280) - Sensor Driver
