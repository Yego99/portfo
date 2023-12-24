from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         name = data["name"]
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{name},{email},{subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"] 
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET']) #We can send data with get by attaching it to the URL
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return'form submitted'
        except:
            return 'did not save to database'
    else:
        return 'UUUhhhh-OOOOhhhh'






    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)