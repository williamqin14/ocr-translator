import ollama
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'Hello there! How are you?',
  },
])
print(response['message']['content'])