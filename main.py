"""Name: Angeline Dorvil
Date: 01/09/2024
Assignment Title: Vaccinations Tracking Procedural Python Assignment
"""

#Get input from the user and validate it using the provided function, to make sure that program does not crash when it receives an invalid input 
def get_valid_input(prompt, validation_func):
  while True:
      user_input_str = input(prompt).strip()
      if validation_func(user_input_str):
          return user_input_str
      else:
          print("Invalid input. Please try again.") #gives users a chance to continue attempting so that the program does not have to start over

#getting individual info for record creation
def gather_individual_data(vac_data_list):
  print()
  print("Enter data for an individual: ")
  user_name = get_valid_input("Enter individual's name: ", lambda x: len(x) > 0 and not x.isdigit()) 
  user_vac_1 = get_valid_input(f"Did '{user_name}' obtain vac_1? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_1 = int(user_vac_1)
  user_vac_2 = get_valid_input(f"Did '{user_name}' obtain vac_2? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_2 = int(user_vac_2)
  user_vac_3 = get_valid_input(f"Did '{user_name}' obtain vac_3? Enter 0 for no and 1 for yes: ", lambda x: len(x) > 0 and x.isdigit() and 0 <= int(x) <= 1)
  user_vac_3 = int(user_vac_3)

  vaccine_data_create(user_name, user_vac_1, user_vac_2, user_vac_3, vac_data_list) #create record
  print()
  print(f"Record created for '{user_name}'.") #confirm creation to user
  print()
  
#create a record using a dictionary for each individual
def vaccine_data_create(name, vac_a, vac_b, vac_c, vac_data_list):
  individual_record_dic = {'name' :name, 'vac_a' :vac_a, 'vac_b' :vac_b, 'vac_c' :vac_c}
  vac_data_list.append(individual_record_dic)
  return vac_data_list

#getting vaccine record for an individual by ther name
def vaccine_record(name, vac_data_list):
  new_data_list = []
  for data in vac_data_list:
    if name in data['name']:
      new_data_list.append(data)

  if new_data_list:
    vaccine_print_record(new_data_list, new_data_list[0]['vac_a'], new_data_list[0]['vac_b'], new_data_list[0]['vac_c'])
  else:
    print()
    print(f"Record not found for '{name}'.")
  print()

#Output modification for vaccine record where vaccine status are in yes/no format to increase user friendliness. this function will be used to show the results in the vaccine_record function
def vaccine_print_record(list, attribute1, attribute2, attribute3):
  vac1_str = ""
  vac2_str = ""
  vac3_str = ""
  if attribute1 == 1:
    vac1_str = 'yes'
  else:
    vac1_str = 'no'

  if attribute2 == 1:
    vac2_str = 'yes'
  else:
    vac2_str = 'no'

  if attribute3 == 1:
    vac3_str = 'yes'
  else:
    vac3_str = 'no'
    
  for data in list:
    print()
    print("Name:",list[0]['name'], "vac_1:",vac1_str, "vac_2:",vac2_str, "vac_3:",vac3_str)
    
  

#getting totals of vaccines
def vaccine_totals(vac_data_list):
  vac_a_count = 0
  vac_b_count = 0
  vac_c_count = 0
  print()
  for data in vac_data_list:
    vac_a_count += data['vac_a']
    vac_b_count += data['vac_b']
    vac_c_count += data['vac_c']
  print(f"vac_a total '{vac_a_count}' \n"
        f"vac_b total '{vac_b_count}' \n" 
        f"vac_c total '{vac_c_count}' ")
  print()

#Main program
def main():
  vac_data_list = []
  while True:
    print("Vaccine tracking procedural program")
    print("----------------------------------")
    print("Make a selection-write the letter corresponding to your choice: ")
    print("i – input data for each individual\n "
          "r – report vaccination data for an individual \n"
          "v – report vaccination totals for each vaccine type \n"
          "q - quit program")
  
    print()
    user_input_str = get_valid_input("Please enter your choice: ", lambda x: 0 < len(x) >= 1 and not x.isdigit()) #taking user's input and validating it
    user_input_str = user_input_str.lower()
  
    if user_input_str == 'i':
      gather_individual_data(vac_data_list)
  
    elif user_input_str == 'r':
      print()
      user_data_report = get_valid_input("Enter the name of an individual to access their record: ", lambda x: len(x) > 0 and not x.isdigit()) #taking user's input and validating it
      user_data_report = user_data_report.lower()
      vaccine_record(user_data_report, vac_data_list)
  
    elif user_input_str == 'v':
      vaccine_totals(vac_data_list)
      
    elif user_input_str == 'q':
      break
      
    else:
      print()
      print("Invalid input. Please try again.")
  
  print("Done!")

if __name__ == "__main__":
  main()