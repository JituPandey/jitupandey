from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    #Dictionary which stores the patientId and its related information
    patients={}
    try:
        #Opening the text file where the information is stored
        with open(fileName,'r') as file:
            for line in file:
                fields = line.strip().split(',')
                
                #If there is no valid no of lines or information
                if len(fields) != 8:
                    print(f"Invalid number of fields ({len(fields)}) in line: {line}")
                    continue
                
                try:
                    #Accessing the datas
                    patient_id = int(fields[0])
                    date = fields[1]
                    temperature = float(fields[2])
                    heart_rate = int(fields[3])
                    respiratory_rate = int(fields[4])
                    systolic_bp = int(fields[5])
                    diastolic_bp = int(fields[6])
                    oxygen_saturation = int(fields[7])
                    
                    #Checking the temperature value within required range
                    if not (35 <= temperature <= 42):
                        print(f"Invalid temperature value ({temperature}) in line: {line}")
                        continue
                    
                    #Checking the hear rate within required range
                    if not (30 <= heart_rate <= 180):
                        print(f"Invalid heart rate value ({heart_rate}) in line: {line}")
                        continue
                    
                    #Checking the respiratory rate within required range
                    if not (5 <= respiratory_rate <= 40):
                        print(f"Invalid respiratory rate value ({respiratory_rate}) in line: {line}")
                        continue
                    
                    #Checking the systolic bp within required range
                    if not (70 <= systolic_bp <= 200):
                        print(f"Invalid systolic blood pressure value ({systolic_bp}) in line: {line}")
                        continue
                    
                    #Checking the diastolic bp within required range
                    if not (40 <= diastolic_bp <= 120):
                        print(f"Invalid diastolic blood pressure value ({diastolic_bp}) in line: {line}")
                        continue
                    
                    #Checking the oxygen saturation within required range
                    if not (70 <= oxygen_saturation <= 100):
                        print(f"Invalid oxygen saturation value ({oxygen_saturation}) in line: {line}")
                        continue
                    
                    if patient_id not in patients:
                        patients[patient_id] = []
                    
                    #Adding the datas to the dictionary
                    patients[patient_id].append([date, temperature, heart_rate, respiratory_rate, systolic_bp, diastolic_bp, oxygen_saturation])
                
                #Handling exception
                except ValueError:
                    print(f"Invalid data type in line: {line}")

    #Handling exception            
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    
    #Handling exception
    except Exception :
        print("An unexpected error occurred while reading the file.")

    return patients
#Name of the text file
fileName='patients.txt'

#--- end of readpatientsfromfile ---#

def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #for all the patients information
    if patientId == 0:
        for patient_id, visits in patients.items():
            print(f"Patient ID: {patient_id}")
            for visit in visits:
                #Printing the information
                print(f"  Visit Date: {visit[0]}")
                print(f"    Temperature: {visit[1]} C")
                print(f"    Heart Rate: {visit[2]} bpm")
                print(f"    Respiratory Rate: {visit[3]} bpm")
                print(f"    Systolic Blood Pressure: {visit[4]} mmHg")
                print(f"    Diastolic Blood Pressure: {visit[5]} mmHg")
                print(f"    Oxygen Saturation: {visit[6]} %")
                print()

    #For single patient information            
    elif patientId in patients:
        print(f"Patient ID: {patientId}")
        for visit in patients[patientId]:
            #Printing the information
            print(f"  Visit Date: {visit[0]}")
            print(f"    Temperature: {visit[1]} C")
            print(f"    Heart Rate: {visit[2]} bpm")
            print(f"    Respiratory Rate: {visit[3]} bpm")
            print(f"    Systolic Blood Pressure: {visit[4]} mmHg")
            print(f"    Diastolic Blood Pressure: {visit[5]} mmHg")
            print(f"    Oxygen Saturation: {visit[6]} %")
            print()

    #If patientId not found
    else:
        print(f"Patient with ID {patientId} not found.")
    
    return patients

#--- end of displaypatientdata ---#

def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    #Exception Handling
    try:
        # type casting the patientId into suitable type
        patientId = int(patientId)

        # if else conditions to check the status of patientId for printing the stats accordingly
        if patientId == 0:
            # calculating average of all patients data
            avg_temperature = sum(visit[1] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())
            avg_heart_rate = sum(visit[2] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())
            avg_respiratory_rate = sum(visit[3] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())
            avg_systolic_bp = sum(visit[4] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())
            avg_diastolic_bp = sum(visit[5] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())
            avg_oxygen_saturation = sum(visit[6] for visits in patients.values() for visit in visits) / sum(len(visits) for visits in patients.values())

            # printing the average vital signs for all patients
            print("Vital Signs for All Patients:")
            print("  Average Temperature:", round(avg_temperature, 2), "°C")
            print("  Average Heart Rate:", round(avg_heart_rate, 2), "bpm")
            print("  Average Respiratory Rate:", round(avg_respiratory_rate, 2), "bpm")
            print("  Average Systolic Blood Pressure:", round(avg_systolic_bp, 2), "mmHg")
            print("  Average Diastolic Blood Pressure:", round(avg_diastolic_bp, 2), "mmHg")
            print("  Average Oxygen Saturation:", round(avg_oxygen_saturation, 2), "%")

        elif patientId in patients:
            visits = patients[patientId]
            if not visits:
                print(f"No data found for patient with ID {patientId}.")
                return

            # calculating average of single patient data
            num_visits = len(visits)
            avg_temperature = sum(visit[1] for visit in visits) / num_visits
            avg_heart_rate = sum(visit[2] for visit in visits) / num_visits
            avg_respiratory_rate = sum(visit[3] for visit in visits) / num_visits
            avg_systolic_bp = sum(visit[4] for visit in visits) / num_visits
            avg_diastolic_bp = sum(visit[5] for visit in visits) / num_visits
            avg_oxygen_saturation = sum(visit[6] for visit in visits) / num_visits

            # printing the average vital signs for single patient
            print(f"Vital Signs for Patient {patientId}:")
            print("  Average Temperature:", round(avg_temperature, 2), "°C")
            print("  Average Heart Rate:", round(avg_heart_rate, 2), "bpm")
            print("  Average Respiratory Rate:", round(avg_respiratory_rate, 2), "bpm")
            print("  Average Systolic Blood Pressure:", round(avg_systolic_bp, 2), "mmHg")
            print("  Average Diastolic Blood Pressure:", round(avg_diastolic_bp, 2), "mmHg")
            print("  Average Oxygen Saturation:", round(avg_oxygen_saturation, 2), "%")
        
        else:
            print(f"Patient with ID {patientId} not found.")

    # exception handling
    except ValueError:
        print("Error: 'patientId' should be an integer.")
    except TypeError:
        print("Error: 'patients' should be a dictionary.")
    except Exception:
        print("An unexpected error occurred while displaying the data.")

#--- end of displaystats ---#

def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    # exception handling
    try:
        # Convert patientId to integer
        patientId = int(patientId)

        # Check if date is in valid format
        parts = date.split('-')
        if len(parts) != 3:
            print("Invalid date. Please enter a valid date.")
            return
        year, month, day = map(int, parts)
        if not (1900 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
            print("Invalid date. Please enter a valid date.")
            return

        # Convert other input values to appropriate types
        date = str(year) + '-' + str(month) + '-' + str(day)
        temp = float(temp)
        hr = int(hr)
        rr = int(rr)
        sbp = int(sbp)
        dbp = int(dbp)
        spo2 = int(spo2)

    # if conditions to check the data range of patients data
        # Check for invalid temperature range
        if not (35.0 <= temp <= 42.0):
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
            return
        # Check for invalid heart rate range
        if not (30 <= hr <= 180):
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
            return
        # Check for invalid respiratory rate range
        if not (5 <= rr <= 40):
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
            return
        # Check for invalid systolic blood pressure range
        if not (70 <= sbp <= 200):
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
            return
        # Check for invalid diastolic blood pressure range
        if not (40 <= dbp <= 120):
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
            return
        # Check for invalid oxygen saturation range
        if not (70 <= spo2 <= 100):
            print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
            return

        # adding data to the dictionary
        if patientId not in patients:
            patients[patientId] = []
        patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])

        # adding the patient data to the file
        with open(fileName, 'a') as file:
            file.write(f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}")

        print(f"Visit saved for Patient # {patientId}")

    # exception handling
    except ValueError:
        print("Invalid input. Please enter valid values.")
    except Exception:
        print("An unexpected error occured")

#--- end of addPatientData ---#

def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    #To store the visits of the patients
    visits = []
    #Exception Handling
    try:
        for patient_id, patient_visits in patients.items():
            for visit in patient_visits:
                #Accesing the year and month of the visit
                visit_date = visit[0].split('-')
                visit_year = int(visit_date[0])
                visit_month = int(visit_date[1])
                
                #Checking the year and month is matching or not
                if (year is None or visit_year == year) and (month is None or visit_month == month):
                    visits.append((patient_id, visit))
    #Handling errror                
    except Exception as e:
        print("An error occurred while searching for visits:", str(e))
    return visits


#--- end of findvisitbydate ---#


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    #Function to call the visits of the patients that needs follow up
    def follow_up(visit):
        _, temp, hr, rr, sbp, dbp, spo2 = visit
        #Checking for any abnormal health stats
        return temp < 30 or hr < 60 or rr < 15 or sbp < 110 or dbp < 70 or spo2 < 90
    
    #To store the patients id who needs followup
    followup_patients = []
    #Exception Handling
    try:
        #for loops to acces the the patient id and its visits
        for patient_id, patient_visits in patients.items():
            for visit in patient_visits:
                if follow_up(visit):
                    followup_patients.append(patient_id)
                    break
        return followup_patients
    
    #Handling exception
    except Exception:
        print("An unexpected error occured")

#--- end of findpatientswhoneedfollowup ---#


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    #Exception Handling
    try:
        if patientId in patients:
            patients.pop(patientId)
            #Opening the file to access the datas
            with open(filename, 'w') as file:
                for patient_id, visits in patients.items():
                    for visit in visits:
                        file.write(f"{patient_id},{','.join(map(str, visit))}\n")

    #Handling exception            
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
    
    #Handling exception
    except Exception :
        print("An unexpected error occurred while reading the file.")

#--- end of deleteallvisitsofpatients ---#


###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
