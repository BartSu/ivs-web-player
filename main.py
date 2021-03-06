# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template

import query

app = Flask(__name__)

import setting
app.config.from_object('setting.Config')

@app.route('/')
def index():
    channel_name = app.config['CHANNEL_NAME']
    cdn_prefix = app.config['CDN_PREFIX']
    media_suffix = app.config['MEDIA_SUFFIX']
    print(f"address from {channel_name}")
    address = query.query_address(channel_name)
    address = cdn_prefix + address + media_suffix
    print(address)
    return render_template("index.html", address=address)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run('0.0.0.0')
