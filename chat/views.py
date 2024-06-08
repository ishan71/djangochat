from django.shortcuts import render, redirect 
from chat.models import Room, Message 
from django.http import HttpResponse, JsonResponse

# Create your views here.
def userlogin(request):
    return render(request, 'userlogin.html')

def home(request):
    return render(request, 'home.html')

def room(request, room):
     username = request.GET.get('username')
     room_details = Room.objects.get(name=room)
     return render (request, 'room.html' , 
    {
        'username' : username,
        'room' : room ,
        'room_details' : room_details
     })

def checkview(request):
    #if request.method == 'POST':
        room = request.POST['room_name']
        username = request.POST['username']
        
        # Check if the room exists
        if Room.objects.filter(name=room).exists():
            
        #if room_obj is not None:
            # If the room exists, redirect the user to the room page
            return redirect('/' +room+'/?username='+username)
        else:
            # If the room doesn't exist, create a new one
            new_room = Room.objects.create(name=room)
            new_room.save()
            return redirect('/' +room+'/?username='+username)

    #return HttpResponse('Failed to create room.')
    
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
    
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    
    messages = Message.objects.filter(room=room_details.id)   
    return JsonResponse({"messages":list(messages.values())}) 