import ollama
import gamer
import json

response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Translate the following Japanese text into English, correcting any syntax or grammatical errors. Put it in the format of a JSON object. Put the the Japanese in one key-value pair, and the English in another key-value pair.' + gamer.ocr('test.jpg'),
  },
])
# print(response['message']['content'])
print(json.loads(response['message']['content']).get('English'))