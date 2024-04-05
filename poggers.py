import ollama
import gamer
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': gamer.ocr('test.jpg'),
  },
])
print(response['message']['content'])