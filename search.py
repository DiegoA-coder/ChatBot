import requests
import json   

class Search:

    list_note=[]
    list_videos=[]
    list_galleries=[]
    list_sections=[]
    dictionary={"notas":None,"galerias":None,"videos":None}  

    @classmethod
    def save_item(cls,title,contentId,link,type,section):
        if (title != "" and contentId != "" and link != "" and type != "" and section != ""):
            itemdictionary={"link":link,"contentId":contentId,"title":title,"section":section}
            if (type=="article"):
                cls.list_note.append(itemdictionary)
            elif (type=="gallery"):
                cls.list_galleries.append(itemdictionary)
            elif (type=="video"):
                cls.list_videos.append(itemdictionary)

    @classmethod
    def update_dictionary(cls):
        cls.dictionary.update({"notas": cls.list_note})
        cls.dictionary.update({"galerias": cls.list_galleries})
        cls.dictionary.update({"videos": cls.list_videos})

    @classmethod
    def request(cls,link):
        try:
            result= requests.get(link)
            statusCode=result.status_code
            if (statusCode == 200):
                return result.json()
            else:
                print("Error occurred in request")
                return None
        except Exception as err:
            print(f'Error occurred in request: {err}')
            return None
    
    @classmethod
    def find_news(cls,word):
        cls.empty_lists()
        link= "https://www.tvazteca.com/aztecanoticias/busqueda?q="+word+ \
            "&_renderer=json"
        jsonRequest=cls.request(link)

        if(jsonRequest != None):
            try:
                results = jsonRequest["results"]
            except Exception as err:
                print(f'Error occurred: {err}')  
                return cls.dictionary;

            for itemResult in results:
                try:
                    title=itemResult["title"]
                    contentId=itemResult["contentId"]
                    link =itemResult["url"]
                    section=itemResult["category"]
                    type=itemResult["type"]
                    cls.save_item(title,contentId,link,type,section)
                except Exception as err:
                    print(f'Error occurred: {err}')

        cls.update_dictionary()
        return cls.dictionary
    
    @classmethod
    def empty_lists(cls):
        cls.list_note=[]
        cls.list_videos=[]
        cls.list_galleries=[]
        cls.dictionary={"notas":None,"galerias":None,"videos":None}  

print(Search.find_news("videos"))