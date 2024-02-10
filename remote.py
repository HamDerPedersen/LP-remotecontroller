from flask import Flask, request, jsonify  # Importerer Flask-klasse, request-objektet og jsonify-funktionen fra Flask-modulet
import subprocess  # Importerer subprocess-modulet til at udføre systemkommandoer
import webbrowser  # Importerer webbrowser-modulet til at åbne URL'er i standardwebbrowseren
import os  # Importerer os-modulet til at arbejde med filsystemet

app = Flask(__name__)  # Opretter en Flask-applikation med navnet '__name__'

@app.route('/shutdown', methods=['POST'])  # Definerer en rute '/shutdown' til at håndtere POST-anmodninger
def shutdown():
    #subprocess.call(['shutdown', '-h', 'now'])  # Udfører kommandoen 'shutdown -h now' for at slukke systemet
    return 'Shutting down...'  # Returnerer en bekræftelsesbesked

@app.route('/restart', methods=['POST'])  # Definerer en rute '/restart' til at håndtere POST-anmodninger
def restart():
    #subprocess.call(['shutdown', '-r', 'now'])  # Udfører kommandoen 'shutdown -r now' for at genstarte systemet
    return 'Restarting...'  # Returnerer en bekræftelsesbesked

@app.route('/open_url', methods=['POST'])  # Definerer en rute '/open_url' til at håndtere POST-anmodninger
def open_url():
    url = request.form.get('url')  # Henter URL'en fra formdata i anmodningen
    if url:
        webbrowser.open(url)  # Åbner den modtagne URL i standardwebbrowseren
        return f'Opening URL: {url}'  # Returnerer en bekræftelsesbesked
    else:
        return 'No URL provided in the request.'  # Returnerer en fejlbesked, hvis der ikke blev angivet nogen URL i anmodningen

@app.route('/open_file', methods=['POST'])  # Definerer en rute '/open_file' til at håndtere POST-anmodninger
def open_file():
    file_path = request.form.get('file_path')  # Henter filstien fra formdata i anmodningen
    if file_path:
        if os.path.exists(file_path):  # Kontrollerer om filen eksisterer på den angivne sti
            os.startfile(file_path)  # Åbner den angivne fil på værtsmaskinen (Kun for Windows-platformen)
            return f'Opening file: {file_path}'  # Returnerer en bekræftelsesbesked
        else:
            return f'File not found: {file_path}', 404  # Returnerer en fejlbesked, hvis filen ikke findes
    else:
        return 'No file path provided in the request.'  # Returnerer en fejlbesked, hvis der ikke blev angivet nogen filsti i anmodningen

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Starter Flask-app'en og lytter på alle IP-adresser på port 5000, når scriptet køres direkte (ikke importeres som en modul)
