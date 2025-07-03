from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    # print("---------------------")
    # print("Logged-in signals----------")
    ip=request.META.get("REMOTE_ADDR")
    # print("CLIENT IP IS : ",ip)
    request.session['ip']=ip
    # version help us to store count for specific user
    ct=cache.get('count',0,version=user.pk)
    newcount=ct+1
    cache.set('count',newcount,60*60*24,version=user.pk)
    print(user.pk)
