import requests
import json 


dictionary={"notas":None,"galerias":None,"videos":None}
listNote=[]
listVideos=[]
listGalleries=[]

def lambda_function(event,context):
    try:
        proxi_event= __build_proxy_event(event)
        if proxi_event.get('word',None):
            return buildHttpResponse(find_news(proxi_event['word']),200)
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

def find_news(word):
    listNote=[]
    listVideos=[]
    listGalleries=[]
    dictionary={"notas":None,"galerias":None,"videos":None}
    link= "https://www.tvazteca.com/aztecanoticias/busqueda?q="+word+"&_renderer=json"
    
    jsonRequest=request(link)

    if(jsonRequest != None):

        try:
            results = jsonRequest["results"]
        except Exception as err:
            print(f'Error occurred: {err}')  
            return newJson();

        for i in range(len(results)):
            try:
                title=results[i]["title"]
                contentId=results[i]["contentId"]
                link =results[i]["url"]
                type=results[i]["type"]
                saveItem(title,contentId,link,type, listNote, listVideos, listGalleries)
            except Exception as err:
                print(f'Error occurred: {err}')
    dictionary.update({"notas": listNote})
    dictionary.update({"galerias": listGalleries})
    dictionary.update({"videos": listVideos})
    return dictionary

def saveItem(title,contentId,link,type, listNote, listVideos, listGalleries):
    if (title != "" and contentId != "" and link != "" and type != ""):
        itemdictionary={"link":link,"contentId":contentId,"title":title}
        if (type=="article"):
            listNote.append(itemdictionary)
        elif (type=="gallery"):
            listGalleries.append(itemdictionary)
        elif (type=="video"):
            listVideos.append(itemdictionary)

def request(link):
    try:
        result= requests.get(link)
        statusCode=result.status_code
        if (statusCode == 200):
            return result.json()
        else:
            print("Error occurred in request")
            return None
    except Exception as err:
        print(f'Error occurred: {err}')
        return None

