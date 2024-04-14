from flask import Flask, jsonify, json
from config import key
import openai
from flask import render_template

openai.api_key = key

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  '''
  response = openai.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1,
  )
  image_url = response.data[0].url
  '''
  image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-k0tFtfiIXYB4BwrSJa8Oq0PF/user-NFCP00xgiGEPfg8fx7SIaGEh/img-THCwNsKJuIuIOr5wyOaeqp3x.png?st=2024-03-10T06%3A55%3A28Z&se=2024-03-10T08%3A55%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-09T18%3A14%3A57Z&ske=2024-03-10T18%3A14%3A57Z&sks=b&skv=2021-08-06&sig=4zUJM4p7OsMYvcac9VNnpTZs%2Bud6EAV6Ksn7m1bkZpQ%3D"
  #print(response)
  return jsonify(image_url)
  #print(image_url)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
