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

@app.route('/btech')
@app.route('/btech/<path>')
def path(path = ""):
    """Summary

    this function is used to render the path of the btech folder

    Args:
        path (str): path of the folder

    """
    folder_data = data

    current_path = list(
        filter(
            lambda x : x.strip() != "", 
            path.strip().split('-')
        )
    )

    for required_folder in current_path:
        if required_folder in folder_data["folders"]:
            folder_data = folder_data["folders"][required_folder]
        else:
            raise KeyError("key not found")

    
    if folder_data.get('is_file_folder', False) == False:

        result_folders = []
        for subfolder_name, subfolder_data in folder_data["folders"].items():
            result_folders.append([
                subfolder_name,
                "-".join(current_path + [subfolder_name]),
                subfolder_data.get('is_file_folder', False)
            ])

        return render_template(
            'explorer.html', 
            title = path,
            path = path, 
            folders = result_folders
        )
    else:
        return redirect(folder_data["link"])
        return webbrowser.open_new_tab(folder_data["link"])

    # except KeyError:
    #     return "Error"

    return render_template('explorer.html', path=path, title = path, sems = range(1, 11))

if __name__ == '__main__':
    app.run(debug=True)