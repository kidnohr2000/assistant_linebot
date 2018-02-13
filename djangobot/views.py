# -*- coding: utf-8 -*-
# vim:tabstop=4:shiftwidth=4:expandtab

from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage
from module.speaker import Talking

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@method_decorator(csrf_exempt, name='dispatch')
class JSONView(TemplateView):

    def get(self, request):
        # request_json = json.loads({'test': 'Hello World'})  # requestの情報をdict形式で取得
        return JsonResponse({'test': 'Hello World'})

    def post(self, request, *args, **kwargs):
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                text2 = event.message.text
                text = Talking(text2)
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=text.greeting())
                )
        return HttpResponse()
