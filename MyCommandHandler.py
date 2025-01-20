from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ChatPermissions
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from Config import config
from keyboard import return_keyboard
from models import V2User
from v2board import _bind, _checkin, _traffic, _lucky, _unbind, _wallet
from Utils import START_ROUTES, END_ROUTES


# 签到
async def command_checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = _checkin(update.effective_user.id)
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    return START_ROUTES


# 绑定
async def command_bind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 打印用户数据
    print(context.user_data)
    
    # 定义键盘
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # 检查是否为私聊
    if update.message.chat.type != 'private':
        text = '绑定用户仅限私聊使用，请私聊机器人'
        await update.message.reply_text(text=text, reply_markup=reply_markup)
        return START_ROUTES
    else:
        try:
            # 获取token
            token = context.args[0].split('token=/')[-1]
        except:
            text = '参数错误，请发送"/bind 订阅链接"'
            await update.message.reply_text(text=text, reply_markup=reply_markup)
            return START_ROUTES
    
    # 调用 _bind 进行绑定操作
    text = _bind(token, update.effective_user.id)
     # 打印 _bind 返回的内容，帮助调试
        print(f"_bind 返回的内容: {text}")
    if text == '绑定成功':
        # 获取用户的 chat_id, user_id 和 verify_type
        chat_id = context.user_data['chat_id']
        user_id = context.user_data['user_id']
        verify_type = context.user_data['verify_type']
        
        # 如果 verify_type 是 'prohibition'，则限制用户发送消息
        if verify_type == 'prohibition':
            permissions = ChatPermissions(can_send_messages=True, can_send_media_messages=True,
                                          can_send_other_messages=True)
            await context.bot.restrict_chat_member(chat_id=chat_id, user_id=user_id, permissions=permissions)
        # 如果 verify_type 是 'out'，解除禁言
        elif verify_type == 'out':
            await context.bot.unban_chat_member(chat_id=chat_id, user_id=user_id, only_if_banned=True)
        
        # 设置绑定成功的消息
        text = "绑定成功！\n\n你的账户已经绑定，欢迎使用寻乐云Bot服务！"
    
    else:
        # 如果绑定失败，返回失败原因
        text = f"绑定失败：{text}"

    # 发送消息
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    
    # 返回到初始路由
    return START_ROUTES



# 解绑
async def command_unbind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    if len(context.args) >= 1:
        # 判断是否管理员
        if telegram_id == config.TELEGRAM.admin_telegram_id:
            email = context.args[0]
            v2_user = V2User.select().where(V2User.email == email).first()
            telegram_id = v2_user.telegram_id
    text = _unbind(telegram_id)
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    return START_ROUTES

# 抽奖
async def command_lucky(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    text = _lucky(telegram_id)
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    return START_ROUTES

# 查看钱包
async def command_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    text = _wallet(telegram_id)
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    return START_ROUTES

# 流量查询
async def command_traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id
    text = _traffic(telegram_id)
    keyboard = [
        return_keyboard,
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text=text, reply_markup=reply_markup)
    return START_ROUTES
