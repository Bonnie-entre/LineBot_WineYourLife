import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    TextMessage, 
    MessageEvent, 
    TextSendMessage, 
    StickerMessage, 
    StickerSendMessage, 
    LocationMessage, 
    LocationSendMessage, FlexSendMessage
)

from pydantic import BaseModel
from config import settings

from bar_googlamap import bar_search
from record import TextMsgReply, ShowMyRecords


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="chatbot handle body error.")
    return 'OK'


@handler.add(MessageEvent, message=LocationMessage)
def message_location(event):
    print("----------------------")
    print(event)
    line_bot_api.reply_message(
        event.reply_token, 
        bar_search(event.message.latitude, event.message.longitude)
    )


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    if("show"in event.message.text) or ("Show"in event.message.text):
        print("show", event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token,
            messages=FlexSendMessage(
            alt_text="測試訊息",
            contents={
                "type": "carousel",
                "contents": ShowMyRecords(event.source.user_id)
                },
            )
        )
        return
    elif  ("紀錄" in event.message.text) or ("記錄" in event.message.text) or ("record" in event.message.text) or ("Record" in event.message.text):
        reply = TextMsgReply(event.source.user_id, 1, event.message.text)

    else:
        # reply = TextMsgReply(event.source.user_id, -1, event.message.text)
        reply = event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )
  


@handler.add(MessageEvent, message=StickerMessage)
def sticker_text(event):
    # Judge condition
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id='6136', sticker_id='10551379')
    )