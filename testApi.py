import smartmedia
import json

# GetAssetList
print ('Get Access List with type \'ce\'')
assetList = smartmedia.getAssetList(type='ce')
print ('Found %d assets' % len(assetList['spdata']))
print ('First 5:')
for x in assetList['spdata'][0:5]:
    print (x)

# GetAssetData
myAsset = assetList['spdata'][20]    
print ('\nGet Access Data')
assetData = smartmedia.getAssetData(myAsset['id'])
print (assetData)

# GetAssetData   
print ('\nGet Access Data')
assetData = smartmedia.getAssetData(myAsset['id'])
print (assetData['spdata'])

# Get ChapterList
print ('\nGet Chapter List')
chapterList = smartmedia.getChapterList(myAsset['id'])
print ('Found %d assets' % len(chapterList['spdata']))
print ('First 5:')
for x in chapterList['spdata'][0:5]:
    print (x)

# Get Chapter Details
myChapter = chapterList['spdata'][5]    
print ('\nGet Chapter Details')
chapterDetails = smartmedia.getChapterDetail(myChapter['id'], myChapter['chap'])
print (chapterDetails['spdata'])

