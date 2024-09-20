import json
from flask import Flask, jsonify, Response, abort
from flask_cors import CORS
from pybaseball import playerid_lookup, bwar_bat
from pandas import DataFrame

try:
    from .environment_vars import API_KEYS
except ImportError:
    from environment_vars import API_KEYS

'''
for dev server, run with:
    flask --app random_calls run --debug --host=0.0.0.0 --port=5000

for gunicorn, run with:
    gunicorn -w 4 -b 192.241.148.156:5000 'random_calls:app'
'''
# flask boilerplate and kruft
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = API_KEYS['SECRET_KEY']

app.config['DEBUG'] = True
if app.config['DEBUG']:
    app.config["CACHE_TYPE"] = "null"

'''
playerid_lookup returns a pandas dataframe object with:
0: name_last
1: name_first
2. key_mlbam
3: key_retro
4: key_bbref
5: key_fangraphs
6: mlb_played_first
7: mlb_played_last
'''

# ----------------------------------------------
# routes

def _get_player_id(last_name, first_name, data_source):
    source_num = {
        'mlbam': 2,
        'retro': 3,
        'bbref': 4,
        'fangraphs': 5,
    }
    idd = playerid_lookup(last_name, first_name)
    if idd.empty:
        return "error"
    # print(idd)
    return idd.at[0, data_source]

@app.route("/player_war/")
def player_war():
    # idd = str(_get_player_id('nlor', 'josh', 'bbref'))
    idd = str(_get_player_id('naylor', 'josh', 'key_bbref'))
    if idd == "error":
        return jsonify({'error': 'player not found'})
    df = bwar_bat()
    # result = df[df["player_ID"] == idd][['year_ID']]
    result = df[df["player_ID"] == idd][['year_ID', 'WAR']]
    d = result.to_json(orient='values')
    print(d)
    return jsonify(d)
