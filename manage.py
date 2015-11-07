from flask import Flask, render_template, jsonify, request

from QueryClass import SourceQuery
# helper functions
from functions import findTeams

IP = "192.168.1.155"
PORT = 27015
SERVERS = [
			[IP, PORT],	
			["192.168.1.156", 1337],		
		]

app = Flask(__name__)
app.debug = True

@app.route('/')

# The main view function
def index():

	#query.getInfo()["Hostname"]
	#info = query.getInfo()
	return render_template("index.html", SERVERS=SERVERS) 

@app.route('/getStats', methods=['POST'])

def getStats():
	ip = request.json["ip"]
	port = request.json["port"]

	# establishes an connection with server
	print (ip, port)
	query = SourceQuery(ip, port)

	# gets info from server
	info = query.getInfo()

	# if response == False the server is offline
	if info != False:
		# get players from server and sort them into teams
		teams = findTeams(query.getPlayers())

		# get rules from server. DOES NOT WORK ATM
		#rules = query.getRules()

		# complete dictionary of the server info
		server_info = {
				"ip": ip,
				"port": port,
				"info": info,
				"teams": teams,
			}
	else:
		#server_info.append(False)
		# TODO: find better way to handle no response from server
		return jsonify(**{"false":"false"})
	# respond request with json format
	return jsonify(**server_info)
if __name__ == '__main__':
	app.run()