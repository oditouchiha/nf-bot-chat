from __future__ import unicode_literals

import errno
import os
import sys
import tempfile
from argparse import ArgumentParser

from flask import Flask, request, abort, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

app = Flask(__name__)

line_bot_api = LineBotApi('TKLdzZSV11rbzChUadiXpeuxQ5BzFejbUPKJMXcdWqLqwt8/7FS8m4QA+SjRZG1AbTaigJirxLxsQgLi6lN6+5JAKpPvZv53KcNpA+Ob0s7X6vZtsdL9/9dUO2BJ8GSaz1F5U7gB9d9u2Sc4bSxn/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('561ac1449f8662b0e13431a9f3fb99ab')


@app.route("/callback", methods=['POST'])
def callback():
    print("============RECEIVING CALLBACK=============")
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    # except LineBotApiError as e:
    #     print("Got exception from LINE Messaging API: %s\n" % e.message)
    #     for m in e.error.details:
    #         print("  %s: %s" % (m.property, m.message))
    #     print("\n")
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """

    # line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=event.message.text))

    text = event.message.text

    if text == 'feelsbadman':
            url = 'https://mmorpg.net/wp-content/uploads/2018/11/feelsbadman-300x273.png'
            app.logger.info("url=" + url)
            print("url=" + url)
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(url, url)
            )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
