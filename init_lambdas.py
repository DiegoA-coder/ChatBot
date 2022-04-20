import json
from management.clients.better_news_client import BetterNewsClient
from management.clients.latest_client import LatestClient
from management.clients.search_client import SearchClient

def lambda_function(event,context):
    try:
        resource_event= event['resource'].replace('/','')
        if resource_event == 'search':
            proxi_event= __build_proxy_event(event)
            if proxi_event.get('word',None):
                return buildHttpResponse(SearchClient.perform(proxi_event['word']),200)
            return buildHttpResponse("word paremeter required",500)
        else:
            if resource_event == 'latest':
                return buildHttpResponse(LatestClient.perform(),200)
            if resource_event == 'betternews':
                return buildHttpResponse(BetterNewsClient.perform(),200)
    except Exception as err:
        return buildHttpResponse(str(err),500)

def __build_proxy_event(event):
    event_body = __build_event_body(event)
    return event_body if isinstance(event_body, dict) else json.loads(event_body)

def buildHttpResponse(body,statusCode):
    return {
        'headers':{
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps(__santitized_body(body)),
        'statusCode': statusCode
    }

def __santitized_body(body):
    if isinstance(body, dict):
        return body
    return { 'message': body }
    
def __build_event_body(event):
    if isinstance(event, dict):
        return event.get('body', event)