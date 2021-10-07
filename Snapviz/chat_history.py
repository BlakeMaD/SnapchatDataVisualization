#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Blake Dukes"
__version__ = "0.1.0"
__license__ = "MIT"

filters = ['all', 'to', 'from', 'ghosted']

def get_chat_history(message_filter:str, Heading:str = 'Users', username:str = ''):
    """ Main entry point of the app """
    import pandas as pd
    import heatmap as map
    import json
    from settings import RAW_CHAT_HIST as rch
    from settings import CLEANED_DATA_PATH as cdp
    
    try:
        global filters

        # validate username input
        if message_filter not in filters:
            print('filter not set to valid option')
            return

        if username != '':
            if filter == 'ghosted':
                print('ghosted filter cannot be used with a specified username.')
                print('Please filter by To, From, or All messages when specifying a username')
                return
            username_list = username
        else:
            username_list = get_chat_usernames(message_filter)

        # Opening JSON file
        f = open(rch)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Collect timestamps of sent and received messages for a particular user
        createdlist = []
        if 'Received Chat History' in data and filter != 'to':
            for i in data['Received Chat History']:
                if i['From'] in username_list:
                    createdlist.append([i['Created']])
        if 'Sent Chat History' in data and filter != 'from':
            for i in data['Sent Chat History']:
                if i['To'] in username_list:
                    createdlist.append([i['Created']])

        f.close()

        # Organize data by date and count of messages sent&received for that date. Output as csv
        df = pd.DataFrame(createdlist, columns=['Date'])
        df['Date'] = pd.to_datetime(df['Date'], yearfirst=True)
        df = df.groupby(df['Date'].dt.date).size().reset_index(name='counts')
        df.to_csv(cdp, index=True)

        # load the data and open window
        map.show_map(Heading)

    except Exception as e:
        print('chat_history.py:')
        print(e)

def get_chat_usernames(filter:str) -> set:
    """Collect distinct usernames in chat_history.json as a set"""
    import json
    from settings import RAW_CHAT_HIST as rch

    try:
        global filters

        # Input validation
        if filter.lower() not in filters:
            print('filter not set to valid option')
            return

        # load in chat_history data
        f = open(rch)
        data = json.load(f) # returns JSON object as a dictionary
        f.close()

        # append received and sent history to set
        from_set = set()
        to_set = set()
        if 'Received Chat History' in data:
            for i in data['Received Chat History']:
                from_set.add([i['From']])
        if 'Sent Chat History' in data:
            for i in data['Sent Chat History']:
                to_set.add([i['To']])

        #return results according to filter
        if filter.lower == 'ghosted':
            # return results of full outer join between to and from messages
            only_to = to_set - from_set
            only_from = from_set - to_set
            return only_to + only_from
        elif filter.lower == 'to':
            return to_set
        elif filter.lower == 'from':
            return from_set
        else:
            return to_set + from_set

    except Exception as e:
        print('chat_history.py:')
        print(e)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    try:
        get_chat_history('all','Ramya \(*.*)/', 'ramyamandyam')
    except Exception as e:
        print('chat_history.py:')
        print(e)
