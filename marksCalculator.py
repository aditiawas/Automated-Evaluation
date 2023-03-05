def calc(yesDict, noDict, maxMarks):
	curWeight = 0
	maxWeight = 0
	for keyWord, weight in yesDict.items():
		curWeight += float(weight) 
	for keyWord, weight in noDict.items():
		maxWeight += float(weight) 
	maxWeight += curWeight
	marks = curWeight/maxWeight * maxMarks
	return round(marks * 2) / 2
