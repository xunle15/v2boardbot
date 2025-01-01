from telegram import InlineKeyboardButton

start_keyboard = [
    [
        InlineKeyboardButton(text='💰我的钱包', callback_data='wallet'),
        InlineKeyboardButton(text='📃流量查询', callback_data='traffic'),
    ],
    [
        InlineKeyboardButton(text='✨幸运抽奖', callback_data='lucky'),
        InlineKeyboardButton(text='📒我的订阅', callback_data='sub'),
    ],
    [
        InlineKeyboardButton(text='📅每日签到', callback_data='checkin'),
        InlineKeyboardButton(text='🌐节点状态', callback_data='node'),
    ],
    [
        InlineKeyboardButton(text='🔗订阅链接', callback_data='mysub'),
        InlineKeyboardButton(text='🎰设置下注', callback_data='start_game'),
    ],
    [
        InlineKeyboardButton(text='🎰开奖记录', callback_data='betting_slots'),
        InlineKeyboardButton(text='🎲适当娱乐', callback_data='dice'),
    ],
    [
        InlineKeyboardButton(text='寻乐互联，即刻连接',
                             url='https://cloud.xunle.de')
    ]
]
keyboard_admin = [
    [
        InlineKeyboardButton(text='⚙Bot设置', callback_data='bot_settings'),
        InlineKeyboardButton(text='🔄重载配置', callback_data='setting_reload')
    ],
    [
        InlineKeyboardButton(text='🎮游戏设置', callback_data='game_settings'),
        InlineKeyboardButton(text='✈机场管理', callback_data='v2board_settings')
    ],
]
start_keyboard_admin = keyboard_admin + start_keyboard
return_keyboard = [InlineKeyboardButton('返回菜单', callback_data='start_over')]
