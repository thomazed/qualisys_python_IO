# qualisys_python_IO
This repository provides an interface for connecting to and interacting with a Qualisys Motion Capture system. The main components include a Python class for handling the connection and data retrieval, and supporting functions for processing the motion capture data.

Files
-----
1. qualisys_io.py
   * Purpose: Manages the connection to the Qualisys system and handles the retrieval of position and rotation data.
   * Key Classes/Methods:
     * qualisys_io: Initializes the connection, starts/stops the data stream, and retrieves position and rotation data.
     * connect(): Starts the data streaming process.
     * stop(): Stops the data streaming and disconnects from the system.
     * get_position_rotation(): Retrieves the latest position and rotation data from the Qualisys system.
2. lib.py
   * Purpose: Contains the underlying logic to connect to the Qualisys system and process 6DoF data.
   * Key Functions:
     * run(): Main loop to handle the real-time data processing and streaming.
     * create_body_index(): Parses the XML data to create a dictionary mapping body names to indices.
     * body_enabled_count(): Counts the number of enabled 6DoF bodies.
     * main(): Handles the connection to the Qualisys system, retrieves data, and processes it in real-time.

How to Use
----------
1. 
