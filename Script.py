class script(object):
    START_TXT = """𝙷𝙴𝙻𝙻𝙾 👋 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 😉, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽.. 𝚃𝙷𝙴𝙽 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂 🦾\n\n𝐌𝐘 𝐂𝐑𝐄𝐀𝐓𝐎𝐑 👇👇👇\n<a href=https://t.me/movi2x><b>Kᕼᴜsᕼ</b></a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✮ 𝙼𝚈 𝙽𝙰𝙼𝙴: ᴀᴜᴛᴏꜰɪʟᴛᴇʀʙᴏᴛ </b>
<b>✮ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/movi2x><b>Kᕼᴜsᕼ</b></a>
<b>✮ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✮ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>
<b>✮ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱</b>
<b>✮ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄</b>
<b>✮ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: 𝚅1.0.43</b>
<b>✮ 𝙼𝚘𝚟𝚒𝚎𝚜 𝚌𝚑𝚊𝚗𝚗𝚎𝚕 🍿: <a href=https://t.me/mdiskmovieshd_2022>ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 📥</a></b>
<b>✮ 𝙼𝙾𝚅𝙸𝙴𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙱𝙾𝚃 🎬: <a href=https://t.me/MovieRequestGroup_rebot>𝙼𝙾𝚅𝙸𝙴𝚂 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 🎬</a></b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
<b>DEVS:</b>
- <a href=https://t.me/mdiskmovieshd_2022>ᴍᴏᴠɪᴇꜱ ᴄʜᴀɴɴᴇʟ 📥</a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particular keyword and Kᕼᴜsᕼ  will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Kᕼᴜsᕼ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Kᕼᴜsᕼ  Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Kᕼᴜsᕼ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/tmmainchannel)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙾𝙽/𝙾𝙵𝙵 𝙼𝙾𝙳𝚄𝙻𝙴..</b>
<b>𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙰𝙽𝙳 𝚂𝙰𝚅𝙴  𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙵𝚁𝙾𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚃𝙾 𝙾𝙽 𝙰𝙽𝙳 𝙾𝙵𝙵 𝚃𝙷𝙴 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿.../</b>
<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 :-
<b>›› /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>›› /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>›› /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>›› /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>𝙲𝚁𝙴𝙳𝙸𝚃𝚂 :- <a href=https://t.me/tmmainchannel>𝐓𝐄𝐂𝐇𝐍𝐎 𝐌𝐈𝐍𝐃𝐙</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Kᕼᴜsᕼ
<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code></b>
<b>★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code></b>"""
    DONATE_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 
›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>
⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/movi2x><b>Kᕼᴜsᕼ</b></a> ᚛━━━━━━━━━━━━
›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>
⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/movi2x><b>Kᕼᴜsᕼ</b></a> ᚛━━━━━━━━━━━━"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>★ 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>★ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>★ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>★ 𝐈𝐃 - <code>{}</code></b>
<b>★ 𝐍𝐚𝐦𝐞 - {}</b>

@mdiskmovieshd_2022
"""
