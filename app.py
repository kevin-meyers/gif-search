from flask import Flask, render_template, request

from lib import tenor_api


app = Flask(__name__)


@app.route('/')
def home():
    gifs_json = tenor_api.rand_search()
    gif_urls = [
      (
       result['media'][0]['gif']['url'],
       result['media'][0]['gif']['dims']
       ) for result in gifs_json['results']
    ]
    return render_template('search.html', gif_urls=gif_urls)


@app.route('/search', methods=['POST'])
def search():
    gifs_json = tenor_api.search(request.form.get('query'))
    gif_urls = [
      (
       result['media'][0]['gif']['url'],
       result['media'][0]['gif']['dims']
       ) for result in gifs_json['results']
    ]
    return render_template('search.html', gif_urls=gif_urls)


@app.route('/trending')
def trending():
    gifs_json = tenor_api.search_trending()
    gif_urls = [
      (
       result['media'][0]['gif']['url'],
       result['media'][0]['gif']['dims']
       ) for result in gifs_json['results']
    ]
    return render_template('search.html', gif_urls=gif_urls)
