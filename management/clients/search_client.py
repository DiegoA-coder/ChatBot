from management.services.readers.search_reader import SearchReader

class SearchClient:
  @classmethod
  def perform(cls,word):
    return SearchReader.perform(word)
