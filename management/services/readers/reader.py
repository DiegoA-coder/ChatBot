from datetime import datetime
import locale
      
class Reader:

    # Setea la variable LC_ALL al conjunto de código UTF-8 con descripción español España
    locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
    list_note=[]
    list_videos=[]
    list_galleries=[]
    list_sections=[]
    dictionary={"notas":None,"galerias":None,"videos":None}  

    @classmethod
    def save_item(cls,itemdictionary,type):
        if (type=="article"):
            cls.list_note.append(itemdictionary)
        elif (type=="gallery"):
            cls.list_galleries.append(itemdictionary)
        elif (type=="video"):
            cls.list_videos.append(itemdictionary)

    @classmethod
    def update_dictionary(cls):
        cls.dictionary.update({"notas": sorted(cls.list_note, key=lambda d: datetime.strptime(d["date"], "%d %B, %Y"),reverse=True)})
        cls.dictionary.update({"galerias": sorted(cls.list_galleries, key=lambda d: datetime.strptime(d["date"], "%d %B, %Y"),reverse=True)})
        cls.dictionary.update({"videos": sorted(cls.list_videos, key=lambda d: datetime.strptime(d["date"], "%d %B, %Y"),reverse=True)})
    
    @classmethod
    def empty_lists(cls):
        cls.list_note=[]
        cls.list_videos=[]
        cls.list_galleries=[]
        cls.dictionary={"notas":None,"galerias":None,"videos":None}  