from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
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

    # Get unread messages via custom manager method
    unread_via_manager = Message.unread.unread_for_user(user)

    # Get unread messages via standard filter with only() and select_related()
    unread_direct = Message.objects.filter(receiver=user, read=False)\
        .only('id', 'content', 'timestamp', 'sender_id')\
        .select_related('sender')

    # Combine both querysets using union (to avoid duplicates)
    combined_unread = unread_via_manager.union(unread_direct)

    # Serialize combined queryset
    messages_data = [
        {
            "id": msg.id,
            "content": msg.content,
            "sender": msg.sender.email,
            "timestamp": msg.timestamp.isoformat(),
        }
        for msg in combined_unread
    ]

    return JsonResponse({"unread_messages": messages_data})