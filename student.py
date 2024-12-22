import csv

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def search_student(file_name, name, student_id):
        try:
            with open(file_name, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[0] == name and row[1] == student_id:
                        return True
            return False
        except FileNotFoundError:
            print("Error: The student file does not exist.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def search_status(file_name, name, student_id):
        try:
            with open(file_name, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[0] == name and row[1] == student_id:
                        return row[2]
            return False
        except FileNotFoundError:
            print("Error: The student file does not exist.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False



    def change_status(file_name, name, student_id, new_status):
        updated = False
        rows = []
        try:
            with open(file_name, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    if row[0] == name and row[1] == student_id:
                        row[2] = new_status
                        updated = True
                    rows.append(row)
            if not updated:
                print(f"No student with name {name} and ID {student_id} found.")
                return
            with open(file_name, "w", newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(rows)
            print(f"Homework status for {name} updated to '{new_status}'.")
        except FileNotFoundError:
            print("Error: The student file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

