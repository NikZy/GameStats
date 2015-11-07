from flask import Flask, render_template, jsonify, request

from QueryClass import SourceQuery

IP = "81.166.24.5"
PORT = 27115
SERVERS = [
			{"ip": IP, "port": PORT},
			
			
]

app = Flask(__name__)
app.debug = True
def findTeams(players):
	'''
	Finds the teams by looking at the players "clan tag" (the first 3 letters)

	Examples:
	"aaa NikZy", "aaa Fredrik", "bbb Frank", "bbb Berta" 
						=
	[aaa NikZy, aaa Fredrik,], ["bbb Frank", "bbb Berta"]

	'''
	team1 = []
	team2 = []
	# for those without teamtag
	rest = []
	for p in players:
		if p["Name"] != "GOTV":
			# 
			p["Frags"] = int(p["Frags"]/2)
			n = p["Name"][:3] 
			if (len(team1) < 1 or n == team1[0]["Name"][:3]):
				team1.append(p)
			elif (len(team2) < 1 or n == team2[0]["Name"][:3]):
				team2.append(p)
			else:
				players.append(p)
	#if (len(team1) < 2):
	#	rest.append(team1[1])

	return {"team1": team1, "team2":team2, "rest": rest}

@app.route('/')

# The main view function
def getStats():
	# querys the server to get info
	#query = SourceQuery(IP, PORT)
	#players = query.getPlayers()

	serverlist = []
	for s in SERVERS:
		# establishes an connection with server
		query = SourceQuery(s["ip"], s["port"])

		# gets info from server
		info = query.getInfo()
		
		# if response == False the server is offline
		if info != False:
			# get players from server and sort them into teams
			teams = findTeams(query.getPlayers())

			# get rules from server. DOES NOT WORK ATM
			#rules = query.getRules()

			serverlist.append({
					"info": info,
					"teams": teams,
					#"rules": query.getRules()
				})
		else:
			pass
			#serverlist.append(False)

	#query.getInfo()["Hostname"]
	#info = query.getInfo()
	return render_template("index.html", serverlist=serverlist) 

@app.route('/test', methods=['POST'])

def test():
	for list in request.json["servers"]:
		print(list[0], list[1])
	return ("response")
if __name__ == '__main__':

	app.run()