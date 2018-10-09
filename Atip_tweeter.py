from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import email
from bs4 import BeautifulSoup

from apiclient import errors
from io import BytesIO



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print('Message snippet: %s' % message['snippet'])

    return message
  except Exception as error:
    print('An error occurred: %s' % error)

def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_bytes(msg_str)

    return mime_msg
  except Exception as error:
    print('An error occurred: %s' % error)



def ListMessagesMatchingQuery(service, user_id, query=''):
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except Exception as error:
    print('An error occurred: %s' % error)

def get_message(id_query):
    
    #id_query="A-2018-00155"    


    all_messages = {}
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    user_id = "me"
    all_messages["messages"] = ListMessagesMatchingQuery(service,user_id,query=id_query)
    messageid = all_messages["messages"][0]["id"]


    GetMimeMessage(service,user_id,messageid)

    finalmessage = GetMimeMessage(service,user_id,messageid)
    
    b = email.message_from_string(str(finalmessage))
    if b.is_multipart():
        for payload in b.get_payload():
            # if payload.is_multipart(): ...
            print(payload.get_payload())
    else:
        messagetext = b.get_payload()

    soup = BeautifulSoup(messagetext, 'html.parser')
    
    data=[b.next_sibling for b in soup.findAll('br')]
    tweet = data[17].replace("=\n","")
    tweet = tweet.replace("=E2=80=93","")
    the_agency = data[5].replace("=\n","")

    link = "du94lycnnfr2r.cloudfront.net/cdn-requests/"
    
    if "Finance" in the_agency:
        the_agency = "FIN"
    if "Royal" in the_agency:
        the_agency = "RCMP"
    if "Environment" in the_agency:
        the_agency = "ENV"
    if "Northern" in the_agency:
        the_agency = "INAC"
        
    if "Transport Canada" in the_agency:
        the_agency = "TC"
        
    fullmessage = the_agency+". "+tweet+". "+id_query+" "+"release."+" "+link+id_query+".pdf" 

    return fullmessage