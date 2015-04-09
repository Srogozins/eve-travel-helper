eve-travel-helper
=================
EVE Online travel planning helper tool

### Installation instructions
* Install the dependencies
* Clone the repository to your computer

### Running instructions
* execute eve-travel-helper/src/server.py. Flask server should now be running on http://127.0.0.1:5000/

### Dependencies
* Shell
    * Bash
    * wget
    * unzip
* python
    * sqlite
    * sqlalchemy
    * networkx
    * Testing
        * unittest
        * mock
* DB
    * sqlite3

### Planned Features

* Engine
    * List systems
    * Filter systems by field
    * Calculate path(s) with least amount of jumps between two systems
       * Avoid systems with security status above/below threshold
