import json
import http.client

conn = http.client.HTTPSConnection('paas-gstt-voicenoteio-brash-bilby-fm.mybluemix.net')
headers = {'Content-type': 'application/json'}

def lambda_handler(event, context):
    data = {
        "idUser": event["idUser"],
        "idAudio": event["idAudio"]
    }
    
    jsonData = json.dumps(data)
    conn.request('POST', '/transcript', jsonData, headers)

    response = conn.getresponse()
    jsonD = json.loads(response.read().decode("utf-8"))
    
    text = []
    output = ''
    
    for result in jsonD["results"]:
        text.append(result["alternatives"][0]["transcript"])
        
        
    output = ''.join(text)
    
    
    return {
        "text": output,
    }