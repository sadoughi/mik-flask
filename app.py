from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      ip_address = result['ip']
      port = result['port']





      """
      کد پایتون رو اینجا بنویس 
      آیپی تو متغیر ip_address
      پورت هم توی متغیر port
      ذخیره شده
      """












      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run('0.0.0.0', debug = True)