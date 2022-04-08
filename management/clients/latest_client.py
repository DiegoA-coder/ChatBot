from management.services.readers.latest_reader import LatestReader

class LatestClient:
  @classmethod
  def perform(cls):
    return LatestReader.perform()