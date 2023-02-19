import requests                                                               #importing the library requests

responseA = requests.get("https://httpbin.org/get")                          #get the response from httpbin get method
print(responseA.status_code)                                                 #prints the result that we get from the above request - result 200

responseB = requests.get("https://httpbin.org/geturffuy")                    #get the response from rubbish httpbin method
print(responseB.status_code)                                                 #prints the result that we get from the above request - result 404

print(responseA.text)                                                        #prints the full text of the response
print(responseA.json())                                                      #prints the response in a json format

resp_json = responseA.json()                                                 #put the json response in a variable
del resp_json['origin']                                                      #delete from the json dictionary that is being returned the field 'origin' which contains my IP address
print(resp_json)                                                             #print the resp_json variable


#--------------------------------------------------------
responseC = requests.get("https://httpbin.org/get?name=Denisa&age=25")       #get requests with parameters
print(responseC.url)                                                         #prints the url that we get from the above request

params = {                                                                   #predefine parameters in a dictionary
    "name": "Denisa",
    "age": "25"
}

responseD = requests.get("https://httpbin.org/get", params=params)           #get requests with parameters that are predefined
print(responseD.url)                                                         #prints the url that we get from the above request

respD_json = responseD.json()                                                #put response in json
del respD_json['origin']                                                     #delete 'origin' field from json
print(respD_json)                                                            #print the respD_json variable - there we will see also our parameters that we are sending


#--------------------------------------------------------
payload = {                                                                  #define payload that contains parameters for post request
    "name": "Denisa",
    "age": "25"
}

responseE = requests.post("https://httpbin.org/post", data=payload)          #send post requests, with the payload defined above
print(responseE.url)

respE_json = responseE.json()                                                #put response in json
del respE_json['origin']                                                     #delete 'origin' field from json
print(respE_json)                                                            #print respE_json variable


#--------------------------------------------------------
responseF = requests.get("https://httpbin.org/status/200")                   #get the status code 200 from statuses
print(responseF.status_code)                                                 #print the status code only

responseG = requests.get("https://httpbin.org/status/404")                   #get the status code 404 from statuses
print(responseG.status_code)                                                 #print the status code only

if responseG.status_code == requests.codes.not_found:                        #in this conditional block we can define the case where the status code is 404, without having to remember the actual code
    print("Not Found")                                                       #in the codes module for the requests package we have the constant 'not_found', which equals to 404
else:                                                                        #if the request returns anything than a 404
    print(responseG.status_code)                                             #it will print back the status code


#--------------------------------------------------------
responseH = requests.get("https://httpbin.org/user-agent")                    #get the user-agent
print(responseH.text, "did this work?")                                       #text doesn't work for user-agent for some reason, but the below json works. Well, now it worked, idk what happened earlier
respH_json = responseH.json()                                                 #put response in json
print(respH_json)                                                             #print response. You get back the user agent 

headers = {                                                                   #in cases where the website refuses to serve your user-agent because you are not a browser
    "User-Agent": "HelloWorld/1.1"                                            #you can specify a different user-agent so that you are accepted and served
}
responseI = requests.get("https://httpbin.org/user-agent", headers=headers)   #get the user-agent, with the one specified above
respI_json = responseI.json()                                                 #put response in json
print(respI_json)                                                             #print response. You get back the user agent 


#--------------------------------------------------------
headers1 = {
    "Accept": "image/png"                                                     #you can also specify what kind of image format you want to have returned (in this case png)
}

responseJ = requests.get("https://httpbin.org/image", headers=headers1)       #get the image, with the type specified in the Accept above
print(responseJ.text)                                                         #however, this will return the image in bytes, so we need to save it in an image

with open("myimage.png", "wb") as f:                                          #we specify the name of the image and the corresponding format (here - png) as we want to save it, and the format "with byte"
    f.write(responseJ.content)                                                #then write the content from the response. The image is downloaded as a result.


headers2 = {
    "Accept": "image/jpg"                                                     #you can also specify what kind of image format you want to have returned (in this case jpg)
}
responseK = requests.get("https://httpbin.org/image", headers=headers2)       #get the image, with the type specified in the Accept above

with open("myimage.jpg", "wb") as f:                                          #we specify the name of the image and the corresponding format (here - jpg) as we want to save it, and the format "with byte"
    f.write(responseK.content)                                                #then write the content from the response. The image is downloaded as a result.


#--------------------------------------------------------
responseK = requests.get("https://httpbin.org/delay/3")                       #let's simulate a timeout. Delayed for 3 seconds

resK_json = responseK.json()
del resK_json['origin']
print(resK_json)

responseL = requests.get("https://httpbin.org/delay/5", timeout=3)            #here if there is no response after 3 seconds (timeout value), there will be an exception thrown
                                                                              #we get a read timeout response
resL_json = responseL.json()
del resL_json['origin']
print(resL_json)

