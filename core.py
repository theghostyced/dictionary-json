import requests
from json import loads

"""
  Process:-
    - Get a word from the dictionary.txt file
    - Send the word to the webscraper api and get a meaning of the word
    - use the response to construct a json object
    - Save the json object as a file called dictionary.json
"""

# Dictionary Webscraper URL from https://googledictionaryapi.eu-gb.mybluemix.net/
base_url_path = "https://googledictionaryapi.eu-gb.mybluemix.net/"

def get_word_meaning(word, lang):
  """
    Gets the meaning of a particular via an HTTP request

    Args:
      word(string): the query word parameter we want to use.
      lang(string): the language you want the response to be in.
    
    Returns:
      The function returns a json gotten after making a request to the endpoint
  """

  response = requests.get(f'{base_url_path}?define={word}&lang={lang}')
  unserialized_data = response.text
  if response.status_code == 404:
    return ''
  
  return loads(unserialized_data)


def serialize_word(word):
  """
    Cleans and strips 🧹 out any apostrophe or /n used in a word

    Args:
      word(string): The word we want to serialize
    
    Returns:
      The serialized string
  """

  no_newline = word.rstrip()
  return no_newline.split("'")[0]


def construct_dictionary(cleaned_word):
  """
    Constructs our dictionary file

    Args:
      cleaned_words(list): the list of all cleaned words
    
    Returns:
      The constructed dictionary
  """

  dictionary = dict()

  result = get_word_meaning(cleaned_word, 'en')
  if result == '':
    return

  dictionary[cleaned_word] = result[0]
  
  return dictionary


