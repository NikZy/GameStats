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