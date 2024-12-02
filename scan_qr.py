import cv2
from pyzbar.pyzbar import decode
import openpyxl
import os
import sqlite3
from datetime import datetime

# File paths
excel_file = 'attendance.xlsx'
db_file = 'attendance.db'

# Initialize Excel
if not os.path.exists(excel_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Attendance'
    sheet.append(["Student ID", "Name", "Timestamp"])
    workbook.save(excel_file)

# Initialize SQLite database
def initialize_db():
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            student_id TEXT,
            name TEXT,
            timestamp TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Function to store data in SQLite database
def store_in_db(student_id, name):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO Attendance (student_id, name, timestamp)
        VALUES (?, ?, ?)
    ''', (student_id, name, timestamp))
    connection.commit()
    connection.close()

# Set to track students who have already scanned
scanned_students = set()

def mark_attendance(data):
    # Open the workbook and select the active sheet
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    # Extract student info
    student_info = data.split(', ')
    student_id = student_info[0].split(': ')[1]
    name = student_info[1].split(': ')[1]

    # Check if the student ID is already scanned
    if student_id in scanned_students:
        print(f"Attendance already marked for: {name}")
        return

    # Append new data to Excel
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append([student_id, name, timestamp])
    workbook.save(excel_file)

    # Store data in SQLite
    store_in_db(student_id, name)

    # Add the student ID to the set to prevent duplicate scans
    scanned_students.add(student_id)
    print(f"Attendance marked for: {name}")

def scan_qr_code():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            # Mark attendance only if the student hasn't scanned yet
            mark_attendance(data)
            print(f"Scanned Data: {data}")

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Initialize database
    initialize_db()

    while True:
        print("\n--- Attendance System ---")
        print("1. Start QR Code Scanning")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            scan_qr_code()
        elif choice == '2':
            print("Exiting...")
            breakq
        else:
            print("Invalid choice. Please try again.")