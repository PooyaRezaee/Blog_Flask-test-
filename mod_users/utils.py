import random
from app import redis,mail

def add_to_redis(user,mode):
    token = random.randint(10000,99999)
    name = f'{user.id}{mode.lower()}'
    redis.set(name=name,value=token,ex=14400)

    return token

def send_singup_message(user,token):
    url = url_for('users.confirm_registeration', email=user.email, token=token, _external=True)

    sender = 'flasktuts@ayinmehr.ir'
    recipients = [user.email]
    subject = 'Verify Register in Blog'
    body = f'Hello,<br>Open this URL: {url}.'
    mail.send_message(sender=sender, recipients=recipients, subject=subject, html=body)

def get_token_redis(user,mode):
    name = f'{user.id}{mode.lower()}'

    return redis.get(name=name)

def delete_token_redis(user,mode):
    name = f'{user.id}{mode.lower()}'

    return redis.delete(name)