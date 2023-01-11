import base64, json,hmac
from hashlib import sha1

level = None
levelFile = None

def loadLevel(levelFile):
	global level
	
	level = levelFile[0:len(levelFile)-40:1]			 # Delete HMAC SHA1
	level = base64.b64decode(level)		      # Decode Base64
	level = json.loads(level)					# Load from string json to dict
	
	return level

def getGround(numGround):
	return level["MAIN"]["SUELO"][numGround]

def getObject(numObject):	
	return level["MAIN"]["NIVEL"][numObject]

def setObjectDict(numObject, dict):
	level["MAIN"]["NIVEL"][numObject] = dict

def addObjectDict(dict):
	level["MAIN"]["NIVEL"].append(dict)

def getTube(numTube):
	return level["MAIN"]["TUBERIAS"][numTube]

def addTubeDict(dict):
	level["MAIN"]["TUBERIAS"].append(dict)

def setTubeDict(numTube,dict):
	level["MAIN"]["TUBERIAS"][numTube] = dict

def getTubeSize():
	return len(level["MAIN"]["TUBERIAS"])

def getSettings():
	return level["MAIN"]["AJUSTES"]

def setGround(numGround, set):
	level["MAIN"]["SUELO"][numGround] = set

def getGroundSize():
	return len(level["MAIN"]["SUELO"])
def addGround(dict):
	level["MAIN"]["SUELO"].append(dict)

def setSettingsOnce(nameSettings, name):
	level["MAIN"]["AJUSTES"][0][nameSettings] = name
	
def setSettingsDict(dict):
	level["MAIN"]["AJUSTES"][0] = dict

def getObjectSize():
	return len(level["MAIN"]["NIVEL"])
def getDecoration(numDecoration):
	return level["MAIN"]["DECORACION"][numDecoration]
def getDecorationSize():
	return len(level["MAIN"]["DECORACION"])
def setDecoration(numDecoration):
	level["MAIN"]["AJUSTES"][numDecoration] = dict			
def saveLevel(path = ""):
	global level
	global levelFile
	_key  = b"2559F35097-2021"
	levelN = json.dumps(level)
	levelN = (base64.b64encode(str.encode(levelN))).decode()
	levelString = str(level)
	_hmac = hmac.new(_key, levelString.encode("utf-8"), sha1)
	if path!="":
		levelFile.close()
		levelFile = open(path, "w", encoding="latin-1")
	levelFile.truncate(0)
	levelFile.seek(0)
	levelString = levelN+str(_hmac.hexdigest())
	levelFile.write(levelString)
