from flask import Flask, request, jsonify  # Importing Flask class, request object, and jsonify function from the Flask module
import subprocess  # Importing the subprocess module for executing system commands
import webbrowser  # Importing the webbrowser module to open URLs in the default web browser
import os  # Importing the os module to work with the file system

app = Flask(__name__)  # Creating a Flask application with the name '__name__'

@app.route('/shutdown', methods=['POST'])  # Defines a route '/shutdown' to handle POST requests
def shutdown():
    #subprocess.call(['shutdown', '-h', 'now'])  # Executes the command 'shutdown -h now' to shut down the system
    return 'Shutting down...'  # Returns a confirmation message

@app.route('/restart', methods=['POST'])  # Defines a route '/restart' to handle POST requests
def restart():
    #subprocess.call(['shutdown', '-r', 'now'])  # Executes the command 'shutdown -r now' to restart the system
    return 'Restarting...'  # Returns a confirmation message

@app.route('/open_url', methods=['POST'])  # Defines a route '/open_url' to handle POST requests
def open_url():
    url = request.form.get('url')  # Retrieves the URL from form data in the request
    if url:
        webbrowser.open(url)  # Opens the received URL in the default web browser
        return f'Opening URL: {url}'  # Returns a confirmation message
    else:
        return 'No URL provided in the request.'  # Returns an error message if no URL was provided in the request

@app.route('/open_file', methods=['POST'])  # Defines a route '/open_file' to handle POST requests
def open_file():
    file_path = request.form.get('file_path')  # Retrieves the file path from form data in the request
    if file_path:
        if os.path.exists(file_path):  # Checks if the file exists at the specified path
            os.startfile(file_path)  # Opens the specified file on the host machine (Windows platform only)
            return f'Opening file: {file_path}'  # Returns a confirmation message
        else:
            return f'File not found: {file_path}', 404  # Returns an error message if the file is not found
    else:
        return 'No file path provided in the request.'  # Returns an error message if no file path was provided in the request

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Starts the Flask app and listens on all IP addresses on port 5000 when the script is run directly (not imported as a module)
