from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from subprocess import call
import socket

app = Flask(__name__)

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-fullscreen")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

def get_identifier():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't need to be reachable, just used to select the right adapter
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip.split(".")[-1]


watermark_code = f"""
    const box = document.createElement('div');
    box.innerText = '{get_identifier()}';
    box.style.position = 'fixed';
    box.style.top = '10px';      // use bottom: '10px' for bottom corner
    box.style.right = '10px';    // change to left for left corner
    box.style.background = 'black';
    box.style.color = 'white';
    box.style.padding = '5px 10px';
    box.style.zIndex = '9999';
    document.body.appendChild(box);
"""

driver.execute_script(watermark_code)

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
