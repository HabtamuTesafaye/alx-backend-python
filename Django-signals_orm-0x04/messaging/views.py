from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Message  # adjust import as needed

User = get_user_model()

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return HttpResponse("User and related data deleted successfully.")


@login_required
def unread_messages_list(request):
    user = request.user
    # Use custom manager, then chain .only() and .select_related() to optimize query
    unread_messages = Message.unread.unread_for_user(user).only('id', 'content', 'timestamp', 'sender_id').select_related('sender')

    messages_data = [
        {
            "id": msg.id,
            "content": msg.content,
            "sender": msg.sender.email,
            "timestamp": msg.timestamp.isoformat(),
        }
        for msg in unread_messages
    ]

    return JsonResponse({"unread_messages": messages_data})
