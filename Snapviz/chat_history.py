#!/usr/bin/env python
"""
Module Docstring
"""

__author__ = "Blake Dukes"
__version__ = "0.1.0"
__license__ = "MIT"


def get_chat_history(username, subject):
    """ Main entry point of the app """
    import os
    import pandas as pd
    import heatmap as map
    import json
    from settings import RAW_CHAT_HIST as rch
    from settings import CLEANED_DATA_PATH as cdp
    
    try:

        # Opening JSON file
        f = open(rch)

        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # Collect timestamps of sent and received messages for a particular user
        createdlist = []
        if 'Received Chat History' in data:
            for i in data['Received Chat History']:
                if i['From'] == username:
                    createdlist.append([i['Created']])
        if 'Sent Chat History' in data:
            for i in data['Sent Chat History']:
                if i['To'] == username:
                    createdlist.append([i['Created']])

        f.close()

        # Organize data by date and count of messages sent&received for that date. Output as csv
        df = pd.DataFrame(createdlist, columns=['Date'])
        df['Date'] = pd.to_datetime(df['Date'], yearfirst=True)
        df = df.groupby(df['Date'].dt.date).size().reset_index(name='counts')
        df.to_csv(cdp, index=True)

        map.show_map(subject)

    except Exception as e:
        print('chat_history.py:')
        print(e)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    get_chat_history('ramyamandyam', 'Ramya \(*.*)/')
