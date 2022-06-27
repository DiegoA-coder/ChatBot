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
        cls.dictionary.update({"notas": cls.list_note})
        cls.dictionary.update({"galerias": cls.list_galleries})
        cls.dictionary.update({"videos": cls.list_videos})

    @classmethod
    def empty_lists(cls):
        cls.list_note=[]
        cls.list_videos=[]
        cls.list_galleries=[]
        cls.dictionary={"notas":None,"galerias":None,"videos":None}  