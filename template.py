# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, render_template


app = Flask(__name__)
app.debug = True

Template_dict = {
    '1': 'shadowsocks-config.json',
    '2': 'nginx-flask.json',
}

@app.route('/get_template', methods = ['POST'])
def get_template():
    print request.form
    post_data = dict((key, request.form.getlist(key) if len(request.form.getlist(key)) > 1 else request.form.getlist(key)[0]) for key in request.form.keys())
    return render_template(Template_dict[post_data['template_id']], **post_data)

if __name__ == "__main__":
    app.run()
