import urllib.request, json
import sys,nltk,time

fil=sys.argv[1] #get file name

#https://books.google.com/ngrams/json is the base url, followed by the params

def getURL(query,start,end,corpus,smoothing,sensitivity):
  query='+'.join([w for w in query.split(' ')])
  sensitivity=str(sensitivity).lower()
  url = 'https://books.google.com/ngrams/json?content=%s&year_start=%d&year_end=%d&corpus=%d&smoothing=%d&case_insensitive=%s'%(query,start,end,corpus,smoothing,sensitivity)
  return url

with open(fil,'r') as r: #read file
  l={}
  cont=r.read()
  cont=cont.split('\n')
  cont=cont[:10000] #take first 10k sentences
  for line in cont:
    p=1
    mylist = list(nltk.bigrams(line.split(' '))) #check by bigram,can be modified here.
    for j in mylist:
      time.sleep(3)#not to send too many requests at a time
      GoToURL=getURL(j,2015,2019,26,3,True)
      with urllib.request.urlopen(GoToURL) as url:
        data = json.loads(url.read().decode())
      if len(data) == 0: #bigram doesn't exist
        p*=1e-6 #can be changed as you wish for
        continue
      for i in data:
        if i['type']=='CASE_INSENSITIVE': #we considered all variations
          if sum(i['timeseries'])==0:
            p*=1e-6
          else:
            p*=float(sum(i['timeseries'])/5) # we take an average over the last five years
    l[line]=p
    time.sleep(2)
pickle.dump(l,open('dump.pkl','wb')) #get dictionary stored as a pickle
