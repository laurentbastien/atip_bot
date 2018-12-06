import tweepy
from documentcloud import DocumentCloud
import boto3


def documentcloud_handler(request):
    methodname = documentcloud_handler.__name__
    try:
        client = DocumentCloud('email', 'password')
        obj_list = client.documents.search(request, data=True)
        for i in range(len(obj_list)):
            contrib = obj_list[i].contributor
            if contrib == "Laurent Bastien":
                break
        link = obj_list[i].canonical_url
        
        return link
        
    except Exception as error:
        errormsg = "Error in {}. Error is {}".format(methodname,error)
        print(errormsg)

def dynamo_handler():
    methodname = dynamo_handler.__name__
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        table = dynamodb.Table('tbl_twitter_tweets')
        result = table.scan()
        description = result["Items"][0]["description"]
        tweetid = result["Items"][0]["tweetid"]
        source = result["Items"][0]["source"]
        table.delete_item(Key={'tweetid': tweetid})
        
        return description,tweetid,source
    
    except Exception as error:
        errormsg = "Error in {}. Error is {}".format(methodname,error)
        print(errormsg)

def twitter_handler():
    methodname = twitter_handler.__name__
    try:
        consumer_key=""
        consumer_secret=""
        access_token=""
        access_token_secret=""
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        tweepyapi = tweepy.API(auth)
        
        return tweepyapi
    
    except Exception as error:
        errormsg = "Error in {}. Error is {}".format(methodname,error)
        print(errormsg)
    

def lambda_handler(event,context):
    methodname = lambda_handler.__name__
    try:
        tweepyapi = twitter_handler()
        description,tweetid,source = dynamo_handler()
        link = documentcloud_handler(tweetid)
        tweettext = description+". "+link
        
        tweettext = tweettext.replace("National Defence","DND")
        
        if len(tweettext) > 279:
            tweettext = source +".Description is too long. See link for details. "+link
            
        print(tweettext)
        
        tweepyapi.update_status(tweettext)
        
    except Exception as error:
        errormsg = "Error in {}. Error is {}".format(methodname,error)
        print(errormsg)
