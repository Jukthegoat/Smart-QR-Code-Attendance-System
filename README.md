# Smart-QR-Code-Attendance-System
Project Title: Smart QR Attendance System

Project Issue/Problem to Be Solved:

The Smart QR Attendance System (SQRAS) is designed to address inefficiencies in traditional classroom attendance methods, such as manually calling roll at the start of each class. This system allows students to generate their own QR codes by entering their ID number and name, eliminating the need for lengthy roll calls. For instructors, the system provides tools for scanning QR codes and managing attendance records, saving both time and resources, and ultimately improving classroom productivity.




Current Progress (PDLC: Problem Analysis, Design, etc.):

Problem Analysis:
Identified challenges with traditional attendance methods.
Defined essential features for the QR Code Attendance System.
Design:
Created a flowchart for the system's workflow.
Developed a database schema to store attendance data.
Designed user interfaces for generating and scanning QR codes.
Development:
Developed QR code generation and scanning modules.
Implemented database CRUD operations (Create, Read, Update, Delete) using SQLite3 to manage attendance records.
Ongoing work to add additional features and user interfaces for both students and instructors.
Testing:
Currently testing QR scanning accuracy and database integration.




Project Functions/Features:

Generate QR Code:
Create unique QR codes for students based on their ID and name.
Scan QR Code:
Allow instructors to scan QR codes using a webcam or mobile device to mark attendance.
Save Data:
Store attendance records securely in the database for future reference.
Search:
Search for attendance records by student name, ID, or date.
Update Data:
Modify attendance records if an error is found.
Delete Data:
Remove outdated or incorrect attendance records.
Export Data:
Export attendance records in Excel or CSV formats for reporting.




Expected Pages for the Web Application:

Home Page:
Dashboard for system overview, showing key information and navigation options.
Login/Signup:
Authentication system for admin and user access.
Generate QR Code:
Page for students to generate and download their personalized QR codes.
Scan QR Code:
Interface for instructors to scan QR codes to mark student attendance.
Attendance Records:
Page displaying attendance data, with search and filter functionalities.
Export Reports:
Option to download attendance data in various formats.




Database Applied:

Database Management System: SQLite3
Tables:
Users: Stores user details (ID, Name, Role, Email, Password).
Attendance: Stores attendance records (ID, Date, UserID, Status).
Records:
Initial test data for development.
Dynamic updates via system interaction.




Project Reference/Source:

YouTube Tutorials:
“Smart QR code-based attendance system using Python” by Nafsi: YouTube Link
“QR Code Scanner & Generator with GUI in Python” by NeuralNine: YouTube Link
“Learn Flask in Python – Full Tutorial” by freeCodeCamp.org: YouTube Link
Documentation:
Python QR Code Documentation.
Assistant:
ChatGPT, for guidance and advice.




Uploaded Files:

Code Files:
Smart QR Code Attendance System - Google Drive
Presentation slide (PPTX):
Smart QR Code Attendance System - PPTX
Recorded Video:

Smart QR Code Attendance System - Recorded Video
GitHub Link:
Smart QR Code Attendance System - GitHub




Instructions to Run the Application:

Required Software and Libraries:
Python 3.x
Required Libraries:
Flask:
Install with pip install flask
cv2 (OpenCV):
Install with pip install opencv-python
Werkzeug:
Install with pip install werkzeug
qrcode:
Install with pip install qrcode[pil]
pyzbar:
Install with pip install pyzbar
sqlite3:
This is part of Python's standard library, so no installation is needed.
datetime:
This is part of Python's standard library, so no installation is needed.
openpyxl:
Install with pip install openpyxl
os:
This is part of Python's standard library, so no installation is needed.
io:
This is part of Python's standard library, so no installation is needed.
Installation Instructions:
Install Python from python.org.
Install the necessary libraries above

Configuration Settings:

Add environment variables for database paths if necessary.
Dependencies:
Requires a webcam or external QR code scanner.
Relies on local storage for database operations.
Running the Application:
Step1:
Retrieve all the files from GitHub Here
Or retrieve all the files from Google Drive Here
Step2:
Run the app.py, navigate to http://127.0.0.1:5000, and alt + click on the link



Fill in the required information and select Student
Generate a QR code and download it
Step 3: 
Run the scan_qr.py file, follow the instructions, 
Show the QR to the camera
Step 4:
Run the app.py again
Fill in the required information and choose Admin
Explore the web application by yourself


