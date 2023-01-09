import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5891924161:AAH5bg85u6GOYfbuXI5kzkR7YRfa7g4P_wo")
    
    API_ID = int(os.environ.get("API_ID", 7978114))
    
    API_HASH = os.environ.get("API_HASH", "5f7839feeba133497f24acfd005ef2ec")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1760280598"))

    SESSION_NAME = "NH_URL_Uploader_Bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://OCmm:505953Oc@cluster0.rwt66hd.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
