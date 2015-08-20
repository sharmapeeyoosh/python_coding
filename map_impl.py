my_store = {}
my_reverse_store = {}

def is_number_present(number):
  return find_by_number(number) == 2 

def add_entry_to_store(name, number):
  name = name.lower()
  my_store[number] = name
  if name in my_reverse_store.keys():
    my_reverse_store[name].append(number)
  else:
    my_reverse_store[name] = [number]

def find_by_name(name):
  name = name.lower()
  tuple_list = []
  if name in my_store.values():
    for item in my_reverse_store[name]:
      tuple_list.append((name, item))
    return 2, tuple_list

  # Partial match
  for num_entry in my_store.keys():
    if my_store[num_entry].startswith(name):
      tuple_list.append((my_store[num_entry], num_entry))
  
  return int(len(tuple_list) > 0), tuple_list
  


# returns 1 if prefix match, returns 2 if full match, returns 0 in case of no match
# it returns the list of matching key, value tuples also
def find_by_number(number):
  tuple_list = []
  if number in my_store.keys():
    tuple_list.append((my_store[number], number))
    return 2, tuple_list

  for num_entry in my_store.keys():
    if str(num_entry).startswith(str(number)):
      tuple_list.append((my_store[num_entry], num_entry))
  
  return int(len(tuple_list) > 0), tuple_list

def delete_from_map(name, number):
  if number 
  
  pass
