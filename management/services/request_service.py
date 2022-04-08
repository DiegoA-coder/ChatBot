import requests

class RequestService:

  @classmethod
  def perform(cls,link):
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