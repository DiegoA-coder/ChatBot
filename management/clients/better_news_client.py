from management.services.readers.better_news_reader import BetterNewsReader

class BetterNewsClient:
  @classmethod
  def perform(cls):
    return BetterNewsReader.perform()