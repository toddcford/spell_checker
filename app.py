import numpy as np
from flask import Flask, render_template, request
import os
app = Flask(__name__)
from spell_check import correct_sentence


@app.route('/')
def home():
  return render_template('index.html')

@app.route('/corrected', methods=['POST'])
def corrected():
  mispelled_sentence = request.form['input_sentence']
  output = correct_sentence(mispelled_sentence)
  return render_template('index.html', corrected_text='{}'.format(output))

if __name__ == "__main__":
  app.run(host=os.getenv('IP', '0.0.0.0'), 
          port=int(os.getenv('PORT', 3000)))