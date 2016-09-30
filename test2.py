
from collections import OrderedDict

def winner(listIsHere):
	getFirst = listIsHere[0]
	listIsHere.pop(0)
	toSet = set(listIsHere)
	setLen = len(toSet)
	total = 0
	if setLen<4:
		total = int(getFirst)
	if setLen==4:
		total = int(getFirst)+1
	elif setLen == 5:
		total = int(getFirst)+2
	elif setLen >= 6:
		total = int(getFirst)+4
	return total

def main():
	t = input()
	while t:
		try:
			players = input()
			listOfPlayers = []
			for i in range(0,players):
				listOfPlayers.append(raw_input().split())

			pointsDic= {}
			for i in range(0,players):
				pointsDic[str(i)] = winner(listOfPlayers[i])
			newDic = OrderedDict(sorted(pointsDic.items(), key=lambda t:t[1]))
			checkDic = newDic
			newDicLast = newDic.values()[-1]
			# print newDicLast
			#Do not fucking change the upper code
			#from here you can put your ass in anything.
			whoWins = checkDic.keys()[-1]
			# print checkDic.keys()[-1]
			# print whoWins

			#deleting last from sorted dic
			secDic = newDic
			deleteLastFromDic =  newDic.keys()[-1]
			secDic.pop(deleteLastFromDic)
			secDiclast = secDic.values()[-1]
			# print secDiclast

			if newDicLast==secDiclast:
				print('tie')

			elif whoWins =='0':
				print('chef')
			else:
				whoWins = int(whoWins)
				print (str(whoWins+1))
		except:
			return 0
		t-=1
main()