
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 644598176 # integer value, dont use ""
    API_HASH = "c5850a7b1efe26f5835a1c219e65ed54"
    TOKEN = "6343038860:AAHrtlB4O0ZS6A3qKtMD2KcjT1APf0RAUYA"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2145093972 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "kawaiianimechat"  # Your own group for support, do not add the @
    START_IMG = "https://raw.githubusercontent.com/Ayushdeveloper001/KawaiiMedia/main/IMG_20231207_013828_481.png"
    EVENT_LOGS = ( -1002035959843 )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://BlackHatDev:BlackHatDev@blackhatdev.zk92igo.mongodb.net"
    # RECOMMENDED
    DATABASE_URL = "postgres://znhtmvbr:1Nwa6oa9bn-Lh7wWwg1zsmV3-nIfvl0h@berry.db.elephantsql.com/znhtmvbr"  #A sql database url from elephantsql.com
    CASH_API_KEY = (
        "VXRGGYORNRVWG9HG"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "QO71WZHGIT4V"
    # Get your API key from https://timezonedb.com/api
    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
