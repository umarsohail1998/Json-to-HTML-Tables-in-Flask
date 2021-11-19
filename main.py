from flask import Flask, redirect, url_for, render_template, request
# from flask_restful import Api, Resource
# from json2html import *
import json

app = Flask(__name__)

def json_to_html(d):
    st = ''
    if type(d) is list:
        st += "<table border='1'><tr><td><ul>"
        for x in d:
            st += f'<li>{json_to_html(x)}</li>'
        st += "</ul></td></tr></table>"
    elif type(d) is dict:
        st += '<table border="1">'
        for x, y in d.items():
            st+= f'<tr><th>{x}</th><td>{json_to_html(y)}</td></tr>'
        st += '</table>'
    else:
        st += str(d)
    return st


@app.route('/')
def welcome():
    return json_to_html(json.loads(open('data.json','r').read()))
    # return json2html.convert(json = input)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    











