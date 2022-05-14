from os import environ
from datetime import datetime, timedelta
from dotenv import load_dotenv

import tweepy
import gspread

load_dotenv()

service_account = gspread.service_account(filename='google_secret.json')
spreadsheet = service_account.open_by_key('1SWORF_qDw_MbqRYgsdLSVGkAuFahv8O82Yzw7Dz49zQ')
worksheet = spreadsheet.sheet1

consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_TOKEN']
access_token_secret = environ['ACCESS_TOKEN_SECRET']

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


def get_time_now_normalized():
    return datetime.now()


def check_and_get_tweets():
    tweets = worksheet.get_all_records()
    for row_index, tweet in enumerate(tweets, start=2):
        message = tweet['message']
        time_str = tweet['time']
        done = tweet['done']

        post_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        if not done:
            now = get_time_now_normalized()
            if post_time < now:
                try:
                    client.create_tweet(text=message, user_auth=True)
                    worksheet.update_cell(row_index, 3, 1)
                except Exception as e:
                    print(f"Exception caught: {e}")


if __name__ == "__main__":
    check_and_get_tweets()
