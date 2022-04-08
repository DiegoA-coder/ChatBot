
class Reader:

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
    def empty_lists(cls):
        cls.list_note=[]
        cls.list_videos=[]
        cls.list_galleries=[]
        cls.dictionary={"notas":None,"galerias":None,"videos":None}  