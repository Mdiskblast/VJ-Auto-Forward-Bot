from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "27c900a8bac51da6d0fd91aad09ef779)
      API_ID = int(getenv("API_ID", "29732337"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6561956588:AAFElWnnqYYrgamjMlY3NkFGR_L3RkXb_hU")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001818795877:-1002014221486").replace("\n", " ").split(' '))


# Don't Remove Credit @Mdisk_Blastt
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @Capta1_n
