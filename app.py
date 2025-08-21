from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from subprocess import call

app = Flask(__name__)

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-fullscreen")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        shutdown = request.form.get('shutdown')
        if shutdown == 'shutdown':
            call("sudo shutdown -h now", shell=True)
        elif url != '':
            url = request.form.get('url')
            driver.get(url)
            driver.execute_script("document.body.style.zoom='175%'")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
