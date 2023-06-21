import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6218540981")
    
    API_ID = int(os.environ.get("API_ID", "23321997"))
    
    API_HASH = os.environ.get("API_HASH", "3c0378a72f84d4dfe7d701bba5f3bbaa")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1847110908"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "izrbab3.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
