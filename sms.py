#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:13:00 2023

@author: shahadsami
"""

from twilio.rest import Client

# إعداد معلومات حساب Twilio
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# إنشاء كائن Client من خلال توفير معلومات الاعتماد
client = Client(account_sid, auth_token)

# إرسال رسالة SMS
message = client.messages.create(
    body='Hello, this is a test message!',
    from_='YOUR_TWILIO_PHONE_NUMBER',
    to='RECIPIENT_PHONE_NUMBER'
)

# طباعة معرّف الرسالة بعد إرسالها
print(message.sid)