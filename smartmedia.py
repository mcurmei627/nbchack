import requests
import json

def doRequest(url, payload = {}):
    base_url = 'http://174.129.13.43:9080/smapi/data/'
    full_url = base_url + url
    r = requests.get(full_url, params = payload)
    return json.loads(r.text)

def getAssetList(type):
    if ((type != 'ce') & (type != 'news')):
        raise ValueError('Parameter type must be \'ce\' or \'news\'')      
    url = 'getassetlist.jsp'
    return doRequest(url, payload = { 'type' : type})

def getAssetData(id):
    url = 'getassetdata.jsp'
    return doRequest(url, payload = { 'id' : id})

def getChapterList(id):
    url = 'getchapterlist.jsp'
    return doRequest(url, payload = { 'id' : id})

def getChapterDetail(assetId, chapterId):
    url = 'getchapterdetail.jsp'
    return doRequest(url, payload = { 'id' : assetId, 'chap' : chapterId})

def getSeasonAssets(season, channel):
    url = 'getseasonassets.jsp'
    return doRequest(url, payload = { 'season' : id, 'channel' : channel})

def getTimeCodedData(assetId):
    url = 'gettimecodeddata.jsp'
    return doRequest(url, payload = { 'id' : assetId})

def getSeasonKeywords(season, show):
    url = 'getseasonkeywords.jsp'
    return doRequest(url, payload = { 'season' : season, 'show': show})

def getEpisodeKeywords(id):
    url = 'getepisodekeywords.jsp'
    return doRequest(url, payload = { 'id' : id})

def getAssetKeywordDet(id):
    url = 'getassetkeyworddet.jsp'
    return doRequest(url, payload = { 'id' : id})

def getChapterKeywords(id, chapter):
    url = 'getchapterkeywords.jsp'
    return doRequest(url, payload = { 'id' : id, 'chapter' : chapter})

