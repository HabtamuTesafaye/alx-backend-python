from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Only participants of the conversation can view, modify, or send messages.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'participants'):
            return user in obj.participants.all()
        if hasattr(obj, 'conversation'):
            return user in obj.conversation.participants.all()
        return False

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
