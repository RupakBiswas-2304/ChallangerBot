from pymongo import MongoClient
CONNECTION_STRING = "mongodb+srv://hacker:flag{404}@cluster0.abtw8.mongodb.net/?retryWrites=true&w=majority"
import datetime

def create_challange(req):
    dbclient = MongoClient(CONNECTION_STRING)
    db = dbclient['CSec']
    collection = db['challenge']
    
    now = datetime.datetime.now()
    challange = req
    collection.insert_one(challange)
    print("Challange created!")
        
if __name__ == "__main__":
    now = datetime.datetime.now()
    desc0 = '''
    Lets solve this week's challange! with our new friend, **ChallengerBot**.
    for the avilable commands type **$man**
    There are 4 problems, and you have time until February 12 
    '''
    

    req = {
        "created-at": now,
            "title": "Bi-weekly Challenge Round 3",
            "status" : "active",
            "description": desc0,
            "code":"MXKKJ",
            "files" : "https://drive.google.com/drive/folders/1-4trgNUMC7UB267_ttH0NpE83YVpTMmO?usp=sharing",
            "problems" : {
                "p1" : {
                    "title" : "Hungry Dragon",
                    "description" : "Last night, Njack members were relaxing and enjoying sweets and doughnuts together in IIT Patna. Suddenly a hungry dragon attacked on them and ate some of their food. The members were angry so, they attacked the dragon and managed to capture it. Now they want to know how many sweets and doughnuts it ate.Can you figure how many sweets and doughnuts the dragon ate?  ",
                    "hint" : "Flag Format: njack{X_doughnut_and_Y_sweet}, here X and Y are integers. [ files included in drive ]",
                    "score" : 200,
                    "flag" : "njack{2_doughnut_and_9_sweet}",
                    "top-hackers" : [],
                    "created-at" : now
                },
                "p2" : {
                    "title" : "Force the Flag",
                    "description" : "Got a api which gives the flag of the challenge, but i have to give a pin to get the flag. After some research i found a way to force the flag [ files included in drive ]. Can you help me? ",
                    "score" : 200,
                    "hint": "The pin is 5 digits long and a hex number between 00000 to fffff",
                    "flag" : "njack{wh3n_1n_d0ubt_u$e_brUte_f0rc3}",
                    "top-hackers" : [],
                    "created-at" : now
                },
                "p3" : {
                    "title" : "Login Obsfuscated",
                    "description" : "Rupak and Siddhart developed this login page but they forgot the login username and password. I tried to bruteforce the login panel but its not working. Can you help me find the flag by logging in ?                          N.B- DO NOT bruteforce as it is not working ",
                    "score" : 200,
                    "hint": " link : https://obsficatedit.cozubozu.repl.co/",
                    "flag" : "njack{!_kNeVV_iT_w@$_JSFUCK**_XD}",
                    "top-hackers" : [],
                    "created-at" : now
                },
                "p4" : {
                    "title" : "Do Something Special",
                    "description" : "Sarthak is trying to get a flag from this website but something is wrong with the button. Can you help him find the flag? Hurry !!!",
                    "score" : 200,
                    "hint": " link : https://dosomethingspecial.cozubozu.repl.co/",
                    "flag" : "njack{!_u$ed_Url_EnC0d!ng_XD}",
                    "top-hackers" : [],
                    "created-at" : now
                }
                
        }
    }
    create_challange(req)