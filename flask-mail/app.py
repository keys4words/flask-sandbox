from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Парсинг zakupki.gov', 
                    recipients=['zharnikov.m@yandex.ru', 'info@novmet.ru'],
                    # body='',
                    html='<h1>Заголовок письма</h1><p>Это текст письма</p>',
                    # cc=[],
                    # bcc=[]
                    )

    with app.open_resource('requirements.txt') as f:
        msg.attach('requirements.txt', 'text/html', f.read())
    mail.send(msg)
    return 'Message has been sent!'


@app.route('/bulk')
def bulk():
    users = [{'name': 'First User', 'email': 'keys4words@gmail.com'}]
    
    with mail.connect() as conn:
        for user in users:
            msg = Message('Bulk!', recipients=[user['email']])
            msg.doby = 'Body text'
            conn.send(msg)


if __name__ == "__main__":
    app.run(debug=True)