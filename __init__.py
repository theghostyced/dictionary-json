import core
from pprint import pprint as pp
from json import dump
from multiprocessing import Pool

def main():
  words = open('dictionary.txt', 'r')

  valid_words_store = []

  for word in words:
    if word[0].isupper():
      continue

    serialized_word = core.serialize_word(word)
    valid_words_store.append(serialized_word)

  words.close()

  # Generate a unique list using set
  unique_store = list(set(valid_words_store))
  sorted_store = sorted(unique_store)

  # Remove every none English word in the list e.g èglarè
  cleaned = sorted_store[:len(sorted_store) - 16]

  # Creating 8 different processes to help with the iteration of the 
  # large list
  process = Pool(8)
  contructed_dict = process.map(core.construct_dictionary, cleaned)

  # Close all pool processes and wait for everything to evaluate
  process.close()
  process.join()

  fw = open('sorted_dictionary.json', 'w')

  dump(contructed_dict, fw)

  fw.close()

if __name__ == '__main__':
  main()
