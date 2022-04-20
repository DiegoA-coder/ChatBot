from dataclasses import dataclass
from management.services.readers.reader import Reader
from management.services.request_service import RequestService

class SearchReader(Reader):

  @classmethod
  def perform(cls, word):
    link= "https://www.tvazteca.com/aztecanoticias/busqueda?q="+word+ \
            "&_renderer=json"
    return cls.find(RequestService.perform(link))

  @classmethod
  def find(cls,jsonRequest):
      cls.empty_lists()

      if(jsonRequest != None):
        try:
          results = jsonRequest["results"]
        except Exception as err:
          print('Error occurred: {err}')  
          return cls.dictionary;

        for itemResult in results:
          try:
            title=itemResult["title"]
            contentId=itemResult["contentId"]
            link =itemResult["url"]
            section=itemResult["category"]
            date=itemResult["date"]
            type=itemResult["type"]
            itemdictionary={"link":link,"contentId":contentId,"title":title,"section":section,"date":date}
            cls.save_item(itemdictionary,type)
          except Exception as err:
            print('Error occurred: {err}')
      cls.update_dictionary()
      return cls.dictionary