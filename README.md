eve-travel-helper
=================
EVE Online travel planning helper tool

### Dependencies
* Shell
    * Bash
    * wget
    * unzip
* Python 2.7
* pip
* DB
    * sqlite3

### Installation instructions
* Clone the repository to your computer
* run `eve-travel-helper/scripts/get_sde.sh` to download and extract necessary Static Data Export.
* run `pip install -r eve-travel-helper/requirements.txt` to install python dependencies

### Running instructions
* execute eve-travel-helper/src/server.py. Flask server should now be running on http://127.0.0.1:5000/

### Planned Features

* Engine
    * List systems
    * Filter systems by field
    * Calculate path(s) with least amount of jumps between two systems
       * Avoid systems with security status above/below threshold
