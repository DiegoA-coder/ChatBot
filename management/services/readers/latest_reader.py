from management.services.readers.reader import Reader
from management.services.request_service import RequestService

class LatestReader(Reader):

  @classmethod
  def perform(cls):
    link= "https://www.tvazteca.com/aztecanoticias?_renderer=json"
    return cls.find(RequestService.perform(link))

  @classmethod
  def find(cls,jsonRequest):
      cls.empty_lists()

      if(jsonRequest != None):
        try:
          mains = jsonRequest["main"]
        except Exception as err:
          print('Error occurred in get : ',err)  
          return cls.dictionary;

        for itemResult in mains:
          try:
            main=itemResult["main"]
            for item_main in main:
              main_title=item_main["title"]
              if main_title == "Noticias Recientes":
                tabs= item_main["tabs"]
                for tab in tabs:
                  contents=tab["content"]
                  for content in contents:
                    item= content["items"][0]
                    contentId=item["contentId"]
                    date=item["date"]
                    link =item["url"]
                    section=item["sectionTag"][0]["title"]
                    title=item["title"]
                    typeItem=item["type"]
                    itemdictionary={"contentId":contentId,"date":date,"link":link,"section":section,"title":title}
                    cls.save_item(itemdictionary,typeItem)
          except Exception as err:
            print('Error occurred in item: ',err)
      cls.update_dictionary()
      return cls.dictionary