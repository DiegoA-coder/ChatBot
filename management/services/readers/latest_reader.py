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
          print('Error occurred in get main: {err}')  
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
                    items= content["items"]
                    for item in items:
                      title=item["title"]
                      contentId=item["contentId"]
                      link =item["url"]
                      section=item["category"]
                      type=item["type"]
                      itemdictionary={"link":link,"contentId":contentId,"title":title,"section":section}
                      cls.save_item(itemdictionary,type)
          except Exception as err:
            print('Error occurred in item: ',err)
      cls.update_dictionary()
      return cls.dictionary