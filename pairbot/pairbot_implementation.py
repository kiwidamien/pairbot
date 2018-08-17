example_list = ['Fred', 'Ginger', 'Gillian', 'The Skipper', 'The Professor', 'Maryann']

def get_pairs(class_list, seed):
  modified_list = class_list[:]
  if len(modified_list) % 2 != 0:
    modified_list.append('Solo')

  n = len(modified_list)
  first_half = modified_list[:n//2]
  second_half = modified_list[n//2:]

  for _ in range(seed):
    second_half.append(first_half.pop())
    first_half.insert(1, second_half.pop(0))
  
  return list(zip(first_half, second_half))

if __name__ == '__main__':
  for i in range(5):
    print(get_pairs(example_list, i))    
