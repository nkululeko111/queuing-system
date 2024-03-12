from pyler import notification
import time


def notify_user():
   
    title = 'Dear Customer'
    message = 'You are now number 12'

    notification.notify(title=title, message=message)
