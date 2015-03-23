# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, render_template


app = Flask(__name__)
app.debug = True

Template_dict = {
    '1': 'shadowsocks-server.json',
    '2': 'shadowsocks-client.json'
}

@app.route('/get_hello', methods = ['GET'])
def get_hello():
    print "hello"
    return "hello"

@app.route('/get_template', methods = ['POST'])
def get_template():
    print request.form
    post_data = {
        'template_id': request.form.get('template_id'),
        'server': request.form.get('server'),
        'password': request.form.get('password'),
    }
    return render_template(Template_dict[post_data['template_id']], **post_data)

if __name__ == "__main__":
    app.run()
