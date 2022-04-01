import json   
from search import Search



def lambda_function(event,context):
    try:
        proxi_event= __build_proxy_event(event)
        if proxi_event.get('word',None):
            return buildHttpResponse(Search.find_news(proxi_event['word']),200)
        return buildHttpResponse("word paremeter required",500)
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

print(Search.find_news("videos"))