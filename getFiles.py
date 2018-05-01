from os import walk

def getFiles(path):
	f = []
	for (dirpath, dirnames, filenames) in walk(path):
		f.extend(dirnames)
		break
	return f