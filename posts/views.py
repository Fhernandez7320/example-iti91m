from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime


posts = [
    {
        'title': 'Picture from Nietzy',
        'user': {
            'name': 'Nietzy Cardoza',
            'picture': 'https://i.picsum.photos/id/404/60/60.jpg?hmac=lwzhD_dCmmfxmIzRzpe6zlpqaTDqkWYTB5WY--m-u6k'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/388/300/300.jpg?hmac=vnDPcudsMpVgI2d2TCqZEEaHnHczNJzfl04fQHpZL-A',
    },
    {
        'title': 'Picture from Crecencio',
        'user': {
            'name': 'Crecencio Gameros',
            'picture': 'https://i.picsum.photos/id/473/60/60.jpg?hmac=4UPx2kZtGolEBosWuZJBOgAkBpz_F8ttwQMz3AMd-BA'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/611/300/300.jpg?hmac=EJgvBzCx8e8CIwFeaaLBr3W56RSBPq8uOhwiEdeEMh0',
    },
    {
        'title': 'Picture from Brenda',
        'user': {
            'name': 'Brenda Gutierrez',
            'picture': 'https://i.picsum.photos/id/403/60/60.jpg?hmac=1mL7eZC4buqRuQYMqOw2Pdt74UW314X6pkaHbSBfXak'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/839/300/300.jpg?hmac=_3qtl641-KhyDcOcpQjTRl8MbB0sES_OBhau2yUoRAE',
    },
    {
        'title': 'Picture from Luis',
        'user': {
            'name': 'Luis Hernandez',
            'picture': 'https://i.picsum.photos/id/326/60/60.jpg?hmac=kqQqOQvh-TQO4lgvQO4ObvAcBuT7XxO4kKkcE9iuy3I'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/485/300/300.jpg?hmac=olQHiVzIoMWmV_hqK8mx7joT4g3QbQRUwebJ4yRVEx8',
    },
    {
        'title': 'Picture from Vianey',
        'user': {
            'name': 'Vianey Lopez',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%dth %b, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/743/300/300.jpg?hmac=etOxwclMseIaDm0uF76VFeu27d7MXfDkNVwZQkQ_KVI',
    }
]

@login_required
def list_post(request):
    return render(request,'posts/feed.html',{'posts': posts})