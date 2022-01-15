import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "pyrogrammers"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "📎 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗡𝗼𝘄"
    st_link = "🎥 𝗣𝗹𝗮𝘆 𝗼𝗻𝗹𝗶𝗻𝗲"
    generating_link = "**⏳ 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗸...**"
    bot_channel = "📢 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗖𝗵𝗮𝗻𝗻𝗲𝗹"
    dev_channel = "🤖 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿"
    fast = "🌀 **𝗬𝗼𝘂𝗿 𝗹𝗶𝗻𝗸 𝘀𝗽𝗲𝗲𝗱 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗼𝗼𝘀𝘁𝗲𝗱**"
    update_link = "🌀 𝗕𝗼𝗼𝘀𝘁 𝗹𝗶𝗻𝗸 𝘀𝗽𝗲𝗲𝗱"
    update_limited = (f"⛔ 𝗬𝗼𝘂 𝗰𝗮𝗻 𝘂𝗽𝗱𝗮𝘁𝗲 𝗷𝘂𝘀𝘁 {Config.Max_Fast_Processes} 𝗟𝗶𝗻𝗸 𝗶𝗻 𝗼𝗻𝗲 𝘁𝗶𝗺𝗲, "
                      "𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝘂𝗻𝘁𝗶𝗹𝗹 𝗽𝗿𝗲𝘃𝗶𝗼𝘂𝘀 𝘂𝗽𝗱𝗮𝘁𝗲 𝘁𝗼 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲")
    re_update_link = "🔄 𝗨𝗽𝗱𝗮𝘁𝗶𝗻𝗴 𝗹𝗶𝗻𝗸 𝗮𝗴𝗮𝗶𝗻"
    already_updated = "𝗟𝗶𝗻𝗸 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝘂𝗽𝗱𝗮𝘁𝗲𝗱!"
    wait_update = "⏳ 𝗨𝗽𝗱𝗮𝘁𝗶𝗻𝗴 𝗹𝗶𝗻𝗸..."
    wait = "⏳ 𝗪𝗮𝗶𝘁 𝗮 𝘄𝗵𝗶𝗹𝗲..."
    progress = "⏳"
    file_not_found = "⚠️ 𝗢𝗼𝗽𝘀! 𝗬𝗼𝘂𝗿 𝗳𝗶𝗹𝗲 𝗶𝘀 𝗺𝗶𝘀𝘀𝗶𝗻𝗴, 𝗣𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝘀𝗲𝗻𝗱 𝗶𝘁 𝗮𝗴𝗮𝗶𝗻"
    delete_manually_button = "⚠️ 𝗗𝗲𝗹𝗲𝘁𝗲 𝗶𝘁"
    delete_forbidden = "The bot can't delete messages older than 48 hours, you can delete this message manually"
    force_join = "🤖 𝗜𝗻 𝗼𝗿𝗱𝗲𝗿 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘁𝗼 𝗷𝗼𝗶𝗻 𝘂𝗽𝗱𝗮𝘁𝗲𝘀 𝗰𝗵𝗮𝗻𝗻𝗲𝗹"
