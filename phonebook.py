from map_impl import is_number_present, add_entry_to_store, find_by_name, find_by_number, delete_from_map

def validate_number(number):
  number_present = is_number_present(number)
  return True

def add_entry():
  number = 0
  name = ''
  number_valid = False
  while not number_valid: 
    number = input("Enter number: ")
    number_valid = validate_number(number)

  name = raw_input("Enter name: ")
  add_entry_to_store(name, number)

def find_entry():
  opts = show_find_options()
  x = -1
  entries = []

  if opts == 1:
    number = input("Enter number: ")
    x, entries = find_by_number(number)

  if opts == 2:
    name = raw_input("Enter name: ")
    x, entries = find_by_name(name)

  if x == -1:
    print "Something Terribly Wrong, debug"
    exit()

  if x == 0:
    print "Not found"

  if x == 1:
    print "Partial matches: "
    print_entries(entries)

  if x == 2:
    print "Entry found:"
    print_entries(entries)

  
def print_entries(entries):
  for entry in entries:
    print entry[0]," : ", entry[1]


def delete_entry():
  if find_entry() == 2:
    delete_from_map()

def process_option(opt):
  if opt == 1:
    add_entry()
  if opt == 2:
    find_entry()
  if opt == 3:
    delete_entry()
  if opt > 3 or opt < 1:
    print ("Invalid Input")
  return

def show_options(arr):
  option_correct = False
  user_input = -1
  while not option_correct:
    print "Enter option:"
    for i in range(len(arr)):
      print i+1, arr[i]
    user_input = input()
    if type(user_input) is int and user_input <= len(arr) and user_input >0:
      option_correct = True
  return int(user_input)

def show_menu_options():
   opts = ["Add Entry", "Find Entry", "Delete Entry"]  
   return show_options(opts)

def show_find_options():
   opts = ["Find by Number","Find by Name"]  
   return show_options(opts)

def _phonebook():
  while True:
    opts = show_menu_options()
    process_option(opts)
  
if __name__ == "__main__":
  _phonebook()
