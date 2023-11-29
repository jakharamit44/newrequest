import os

from dotenv import load_dotenv

load_dotenv()

def is_enabled(value, default):

    if value.lower() in ["true", "yes", "1", "enable", "y"]:

        return True

    elif value.lower() in ["false", "no", "0", "disable", "n"]:

        return False

    else:

        return default

class Config(object):

    API_ID = int(os.environ.get("API_ID", "17737898"))

    API_HASH = os.environ.get("API_HASH", "ad762fe0516f367115ba651d929cf429")

    BOT_TOKEN = os.environ.get(

        "BOT_TOKEN", "6511699844:AAFEF1kACN7F9aaIB7HiuJ6ETk9LceXji30")

    OWNER_ID = int(os.environ.get("OWNER_ID", "5702180952"))

    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)

    CHAT_ID = [int(x) for x in os.environ.get(

        "CHAT_ID", "-1001587677801").split()]

    SESSION_STRING = os.environ.get("SESSION_STRING", "BQCPmNm8m5btkEqZFNj74ALumrfNcTigxgcBDBOeDxZByqfo5eEKCuAKJSyFMR5Q6zwPesl603CiOnpRB0Tg59_v8QefERzFPdRZ2Q3HD_-Uy971dAv-a8HMNFsSGVpISlU3Bl7dvdBXNMRjJZ6fYiYegZYAtgSVvSwueWEF9ziKvdnh4lgSg6Oqi55GmCle0GwdGWI3lvjQxvtO4oiPFvS6_hHAFPUUS7SmuAj_CWsPuJYhs-svlyvzkqjii7Nh0YTAK_PY586FMpdkN5hyQYNueGsd051n4JaucF04z7-p2x-ymOVgE-4oT-aWN4Y0YuOww1oOoSALZAH4juC7QfybAAAAAVPgYFgA")

    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://baba:baba@cluster0.etssakc.mongodb.net/?retryWrites=true&w=majority")

    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "telegram")

class Script(object):

    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message I'm Auto Request Accept Bot")

    ACCEPT_MESSAGE = os.environ.get(

        "ACCEPT_MESSAGE", "Your request to join channel has been approved!\n\n Send /start to know more")
