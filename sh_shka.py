def tear(mess, n):
	return [mess[i:i+n] for i in range(0, len(mess), n)]

def intInput(text):
	return map(lambda a: int(a), input(text).split());