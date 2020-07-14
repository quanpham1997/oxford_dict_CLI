import sys
import  requests
from urllib.request import urlopen
import json

class Dict:
    app_id = 'e72676d4'
    app_key = 'c89d764a03f80f3642208e8cbd0f99ef'
    language = 'en'
   # word_id = <word_to_look_up>
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'
    #url Normalized frequency
    #urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' #+ word_id.lower()
    def __init__(self,app_id=app_id,app_key=app_key):
        self.last_search = ""
        self.app_id  = app_id
        self.app_key = app_key

    def get_par(self,Word=""):
        if Word == "" or Word == "q.":
            return "",""
        self.last_search = Word
        URL = self.url + Word
        r = requests.get(URL, headers = {'app_id' : self.app_id, 'app_key' : self.app_key})
        content = json.dumps(r.json())
        content = json.loads(content)
        return Word,content

    def parse(self,Word="",Content=""):
        t = 1
        if Word == "" or Content == "":
            return
        print(f'{Word.upper()} \n ------------------------\n\n')
        for i in Content["results"]:
            for j in i["lexicalEntries"]:
                try:
                    for k in j["entries"]:
                        for v in k["senses"]:
                            print(f'{t}/ {v["definitions"][0]}')
                            t += 1
                            try:
                                for n in v['examples']:
                                    print(f" =>  {n['text']}")
                            except KeyError:
                                continue
                except KeyError:
                    continue

if __name__ == "__main__":
    D = Dict()
    while True :
        try:
            Word,Content = D.get_par(Word=input("Enter word : ").lower())
            if Word == "" or Content == "":
                break
            else:
                D.parse(Word=Word,Content=Content)
        except:
            print("error : {}".format(sys.exc_info()[0]))

