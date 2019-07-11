# -*- coding: utf-8 -*-
import boto3
import os


class Ses:

    def __init__(self):
        session = boto3.Session(region_name="us-east-1")
        self.client = session.client('ses')

    def send(self):
        response = self.client.send_email(
            Source=os.environ['SCRAPING_EMAIL'],
            Destination={
                'ToAddresses': [
                    os.environ['SCRAPING_EMAIL']
                ],
            },
            Message={
                'Subject': {
                    'Data': os.environ['SCRAPING_MAIL_TEXT'],
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': os.environ['SCRAPING_MAIL_TEXT'],
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': '<h1>' + os.environ['SCRAPING_MAIL_TEXT'] + '</h1>',
                        'Charset': 'UTF-8'
                    }
                }
            },
            ReplyToAddresses=[
                os.environ['SCRAPING_EMAIL']
            ])