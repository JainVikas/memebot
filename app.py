# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:11:41 2017

@author: vikas
"""
from flask import Flask, request, jsonify
import os
from pymeme import *

app = Flask(__name__)
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'
meme = MemeGen()
meme.retrieve_api()

templateURL= meme.get_link_templates()
templateDict = meme.get_templates()
exampleUrlList=[]
aliaseList=[]
for key in templateDict:
    template = meme.get_template(key)
    print(template.get_name())
    aliase=template.get_aliases()[1]
    try:
        example = template.get_example(aliase)
        print(example.get_direct_visible())
        exampleUrlList.append(example.get_direct_visible())
    except:
        pass
   
print(exampleUrlList) 
len(exampleUrlList)



def replaceUnderscores(stringInput):
    return stringInput.replace('_'," ")

def splitLink(exampleUrl):
    t= exampleUrl.split(sep='/')
    if len(t)>=6:
        link= t[0]+ '//'+ t[2] +'/'+t[3]+'/'
        upperText= replaceUnderscores(t[4])
        lowerText= replaceUnderscores(t[5].split('.')[0])
    else:
        link= t[0]+ '//'+ t[2] +'/'+t[3]
        upperText= replaceUnderscores(t[4].split('.')[0])
        lowerText=replaceUnderscores('_')
    return link,upperText,lowerText


@app.route('/images', methods=['POST', 'GET'])
def images():
    inputRecords = request.args.get('inputRecords')

    galleryResponse= {
     "messages": [
    {
      "attachment":{
    "type":"template",
    "payload":{
      "template_type":"generic",
      "image_aspect_ratio": "square",
      "elements":[ ]
    }
      }
    }
      ]
    }

    for i in range(9):
        count=i + int(inputRecords)
        resultTemplate={
               "buttons": [
                {
                  "set_attributes": {
                    "imageInput": "some value",
                    "upperText": "another value",
                    "lowerText": "lower text value"
                  },
                  "block_names": [
                    "Routing"
                  ],
                  "type": "show_block",
                  "title": "customise"
                },
                {
                  "type": "element_share"
                }
              ]
            }
        #print(i)
        #print(exampleUrlList[i])
        imageInput, upperText, lowerText = splitLink(exampleUrlList[i])
        #print(imageInput, upperText, lowerText)
        if upperText !=" ":
            resultTemplate['title']= upperText
            resultTemplate['subtitle']= lowerText
        else:
            resultTemplate['title']= lowerText
            resultTemplate['subtitle']= upperText
        resultTemplate['image_url'] = exampleUrlList[i]
            
        resultTemplate["buttons"][0]["set_attributes"]["imageInput"]= imageInput
        resultTemplate["buttons"][0]["set_attributes"]["upperText"]= upperText
        resultTemplate["buttons"][0]["set_attributes"]["lowerText"]= lowerText
        #print(resultTemplate)
        galleryResponse['messages'][0]['attachment']['payload']['elements'].append(resultTemplate)
        #print(galleryResponse)
        
    moreResult= {'title':"want to see more",
           "buttons": [
            {
              "set_attributes": {
                "inputRecords": count+1,
              },
              "block_names": [
                "imageJson"
              ],
              "type": "show_block",
              "title": "show more"
            }
          ]
        }
    galleryResponse['messages'][0]['attachment']['payload']['elements'].append(moreResult)
    return jsonify(galleryResponse)


@app.route('/generateMEME', methods=['POST', 'GET'])
def generateMeme():
    imageInput = request.args.get('imageInput')
    upperText = request.args.get('upperText')
    lowerText = request.args.get('lowerText')
    print(imageInput,upperText,lowerText)
    print( imageInput+upperText+"/"+lowerText+ ".jpg")
    print(type( imageInput+upperText+"/"+lowerText+ ".jpg"))
    result = {
      "messages": [
        {
          "attachment": {
            "type": "image",
            "payload": {
              "url": imageInput+upperText+"/"+lowerText+ ".jpg"
            }
          }
        }
      ]
    }
    return jsonify(result)
if __name__ == '__main__':
  app.debug = True
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port = port)