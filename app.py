from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from json import load, dump
from os import listdir, path, mkdir, remove, rename

app = Flask(__name__)
data = None
with open('data.json', 'r') as f:
    data = load(f)

@app.route('/')
def index():
    """Summary

    this function is used to render the index page
    """
    return render_template('index.html')

@app.route('/btech/<path>')
def path(path):
    """Summary

    this function is used to render the path of the btech folder

    Args:
        path (str): path of the folder

    """
    folder_data = data

    try:
        for folder in path.split('/'):
            print(folder, end = "\n" * 3)
            folder_data = folder_data[folder]
        
        if folder_data['is_folder_file'] == False:
            return render_template(
                'explorer.html', 
                path = path, 
                title = path, 
                folders = folder_data['folders'],
            )
        else:
            return redirect(folder_data['link'])

    except KeyError:
        return render_template('404.html')

    return render_template('explorer.html', path=path, title = path, sems = range(1, 11))

if __name__ == '__main__':
    app.run(debug=True)