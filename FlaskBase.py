from flask import Flask, render_template, request, redirect, url_for, session
from DataManage.DataManage import DataManage

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fhksdy687rh23ihrh'

info = {}
formc = {}
login_status = [False]

@app.route('/log in', methods=['GET', 'POST'])
def login():
    info['message_l'] = 'fill in and log in'
    info['m_name'] = 'logn'
    if request.method == 'POST':
        formc['name_l'] = request.form.get('inputName')
        formc['psw_l'] = request.form.get('inputPsw')
        if DataManage.DataSelect(formc) != []:
            session['name'] = formc['name_l']
            info['message_l'] = 'log in success！'
            info['m_name'] = 'logy'
            login_status[0] = True
        else:
            info['message_l'] = 'login failure!'
            info['m_name'] = 'logn'
            login_status[0] = False
    return render_template('Login.html', info=info)

@app.route('/Reg/', methods=['GET', 'POST'])
def reg():
    info['message_r'] = 'fill in and register'
    if request.method == 'POST':
        formc['name'] = request.form.get('inputName')
        formc['psw'] = request.form.get('inputPsw2')
        formc['email'] = request.form.get('inputEmail')
        formc['tel'] = request.form.get('inputTel')
        if DataManage.DataInsert(formc):
            info['message_r'] = 'register success！'
        else:
            info['message_r'] = 'register failure！'
    return render_template('Reg.html', info=info)

@app.route('/Success/')
def LoginSuccess():
    if login_status[0] == False:
        return redirect(url_for('login'))
    info['user_agent'] = request.headers.get('User-Agent')
    # info['ip'] = request.remote_addr
    info['ip'] = request.headers['X-Forwarded-For']
    return render_template('Success.html', info=info, username=session.get('name'))
@app.route('/main_page')
def main_page():
	return render_template('main_page.html')
@app.route('/model')
def model():
	return render_template('model.html')
@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html')
@app.route('/log in')
def log_in():
	return render_template('Login.html')
@app . errorhandler (404)
def page_not_found ( error ) :
    return " Couldn't find the page you requested .", 404
@app.route('/action')
def action():
	return render_template('action.html')
@app.route('/adventure')
def adventure():
	return render_template('adventure.html')
@app.route('/comedy')
def comedy():
	return render_template('comedy.html')
@app.route('/crime')
def crime():
	return render_template('crime.html')
@app.route('/drama')
def drama():
	return render_template('drama.html')

if __name__ == '__main__':
    app.run(debug=True)