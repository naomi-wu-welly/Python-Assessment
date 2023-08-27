# ============== BRMM Bankside Rakaia Motorkhana Mavens MAIN PROGRAM ==============
# Student Name: Naomi Wu
# Student ID : 1158161
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import brmm_data    # brmm_data.py MUST be in the SAME FOLDER as this file!
                    # brmm_data.py contains the data lists
import datetime     # We are not using date times for this assessment, but it is
                    # available in the column_output() fn, so do not delete this line

# Data variables
col_drivers = brmm_data.col_drivers
db_drivers = brmm_data.db_drivers
col_runs = brmm_data.col_runs
db_runs = brmm_data.db_runs


def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_drivers():
    # List the ID, first name, last name, and age of all drivers

    # Create a dictionary of heading names and types to match the column output
    col_driver_list = {'Driver ID': int, 'First Name': str, 'Surname': str, 'Age': int}
    # Convert the dictionary data into a list that displays the required data fields
    display_list = []
    for driver in db_drivers.keys():
        display_list.append((driver,
                             db_drivers[driver][0],
                             db_drivers[driver][1],
                             db_drivers[driver][3]))
    format_columns = "{: >9} | {: <12} {: <12} | {: ^5}"
    print("\nDRIVER LIST\n")    # display a heading for the output
    column_output(display_list, col_driver_list, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output


def list_juniors_by_age():
    # Print a list of the junior drivers, sorted by Age.
    # Use col_juniors as the column headings.
    # Amend your code to display the caregiver's full name instead of the caregiver's ID
    col_juniors = {'Driver ID': int, 'Driver Name': str, 'Age': str, 'Caregiver Name': str}

    # Complete the function
    # task-2
    db_juniors = []
    for driver in db_drivers.keys():
        # Junior drivers are identified by a 'J'
        if db_drivers[driver][2] == 'J':
            # if driver is a junior and aged 12-16, find the caregiver's name
            if db_drivers[driver][3] >= 12 and db_drivers[driver][3] <= 16:
                caregiver_name = db_drivers[db_drivers[driver][4]][0] + ' ' + db_drivers[db_drivers[driver][4]][1]
            else:
                caregiver_name = 'None'    
            # append the junior driver's details to the list      
            db_juniors.append((driver,
                               db_drivers[driver][0] + ' ' + db_drivers[driver][1],
                               db_drivers[driver][3],
                               caregiver_name))
    # sort the list by age
    db_juniors.sort(key=lambda x: x[2])
    # print out the list
    print('==================== JUNIOR DRIVER LIST ====================')
    column_output(db_juniors, col_juniors, "{: <9}  {: <16}  {: <5}  {: <16}")
    print('==================== ****************** ====================')


def list_runs():
    # Print a list of runs, including the Run Totals.
    # Display in Course order A B C and within that by time (fastest A first, to slowest C last).
    # column headings
    col_runs = {'Run ID': int, 'Course': str, 'Driver': str, 'Time': str, 'Cones hit': str, 'WD status': str, 'Run Total time': str}
    runs_result = []
    for run in db_runs.keys():
        # Driver name
        driver_name = db_drivers[db_runs[run][1]][0] + ' ' + db_drivers[db_runs[run][1]][1]
        # Time
        if db_runs[run][2] is None or db_runs[run][2] < 0:
            run_time = int(0)
        else:
            run_time = float(db_runs[run][2])
        # Cones hit
        if db_runs[run][3] is None or db_runs[run][3] < 0:
            cones_hit = int(0)
        else:
            cones_hit = int(db_runs[run][3])
        # WD status
        if db_runs[run][4] is None or db_runs[run][4] < 0:
            wd_status = int(0)
        else:
            wd_status = int(db_runs[run][4])
        run_total_time = float(run_time + 5 * cones_hit + 10 * wd_status)
        runs_result.append((run,                        # Run ID
                            db_runs[run][0],            # Course
                            driver_name,                # Driver name
                            run_time,                   # Time
                            cones_hit,                  # Cones hit
                            wd_status,                  # WD status
                            run_total_time))            # Run Total time
    
    # sort by course asc, then by run_total_time asc
    runs_result.sort(key=lambda x: (x[1], x[-1]))
    # print out the list
    runs_format = "{: >6} {: ^6} {: <16} | {: <6} {: ^9} {: ^9} | {: <6}"
    print('============================ RUN LIST ============================')
    column_output(runs_result, col_runs, runs_format)
    print('============================ ******** ============================')

def edit_run_results():
    # Display list of runs. Make use of your existing function.
    # Then allow the user to enter a run ID (limited to existing runs), and to update the run data.
    # Add validation so times are in a sensible range, and WD is restricted to 1 or 0.

    pass  # REMOVE this line once you have some function code


def display_final_results():
    # Calculate and display the overall results.
    # Use col_final_results as the column headings. NOTE :
    #   'Driver' is driver ID
    #   'Driver Name' is both names together, e.g., 'Hank Barnard'
    #    Add '(J)' after the name for juniors, e.g., 'Edward Cooper (J)'
    # Order results from best to worst
    # Display any "HAG" results at the bottom
    col_final_results = {'Driver': int, 'Driver Name': str, 'Result': str}

    # Complete the function


def display_cone_graph():
    # List any drivers who hit cones, along with their total numbers of cones as a repeating symbol or character.
    # Do not list any drivers who did not hit any cones.
    

    pass  # REMOVE this line once you have some function code


# function to display the menu
def disp_menu():
    print("==== WELCOME TO BRMM Fun-khana Event ===")
    print(" 1 - List Drivers")
    print(" 2 - List Juniors (by age) including caregivers")
    print(" 3 - List Run Results")
    print(" 4 - Add Run Data")
    print(" 5 - Display Overall Results")
    print(" 6 - Display cones hit graph")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
while response.upper() != "X":
    if response == "1":
        list_drivers()
    elif response == "2":
        list_juniors_by_age()
    elif response == "3":
        list_runs()
    elif response == "4":
        edit_run_results()
    elif response == "5":
        display_final_results()
    elif response == "6":
        display_cone_graph()
    else:
        print("\n***Invalid response, please try again (enter 1-6 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for supporting BRMM, see you at the next event! ===\n")
