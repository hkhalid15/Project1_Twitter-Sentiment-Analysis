# 
# M.Ebanks
#	REQUIRES
#	appkeys.py
#	tmenu1.py
#	locationlist.py (imported into tmenu1)
#


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import time
import json
import csv
import appkeys
import tmenu1 as mt

ckey = appkeys.CONSUMER_KEY
csecret = appkeys.CONSUMER_SECRET
atoken = appkeys.ACCESS_TOKEN
asecret = appkeys.ACCESS_TOKEN_SECRET


class listener(StreamListener):
    def on_data(self, data):
        try:
            data_json = json.loads(data)
            id_str = data_json["id_str"]
            Tweet_time = data_json["created_at"]
            user_name = data_json["user"]["name"]
            Tweet_text = data_json["text"]
            Retweet_count = data_json["retweet_count"]
            Tweet_name = data_json["entities"]["user_mentions"][0]["name"]
            Tweet_fw = data_json["user"]["followers_count"]
            Tweet_fd = data_json["user"]["friends_count"]
            Tweet_st = data_json["user"]["statuses_count"]
            f = csv.writer(open(str(locID)+"_"+str(filenameID)+ ".csv", "a+"),
                           delimiter='|')
            f.writerow([id_str,
                        Tweet_time,
                        user_name,
                        Tweet_text,
                        Retweet_count,
                        Tweet_name,
                        Tweet_fw,
                        Tweet_fd,
                        Tweet_st,
                        coordinates])
            return True

        except Exception as e:
             # print("MSG: " + str(e))
             # time.sleep(5)
             pass


    def on_error(self, status):
        print(status)



# Authorize the API
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


selection   = mt.menu()
locinfo     = mt.getloc(selection)

locID       = str(locinfo["locID"])
coordinates = locinfo["coordinates"]

filenameID = input("Please provide a unique identifier for the output file: ")
print("NOTE: The output file name: " + str(locID)+"_"+str(filenameID)+".csv")

# Call the main function
streamer = Stream(auth, listener())
streamer.filter(locations=coordinates,
                 languages=["en"])

print("-"*30)
print("Selection:  " + str(selection) + " locID:   " + locID)
print("   coords:  " + str(coordinates))
print("  locinfo:  " + str(locinfo))
print("-"*30)


