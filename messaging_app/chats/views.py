from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAuthenticated, IsParticipantOfConversation
from .models import Conversation, Message
from .serializers import (
    ConversationSerializer, ConversationCreateSerializer,
    MessageSerializer, MessageCreateSerializer
)
from .filters import MessageFilter
from .pagination import MessagePagination

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['participants__first_name', 'participants__last_name']
    ordering_fields = ['created_at']

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ConversationCreateSerializer
        return ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MessageFilter
    search_fields = ['message_body', 'sender__first_name', 'sender__last_name']
    ordering_fields = ['sent_at']
    pagination_class = MessagePagination

    def get_queryset(self):
        # Ensure users can only access messages in conversations they are part of
        conversation_id = self.request.query_params.get('conversation_id')
        user = self.request.user

        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id)
            except Conversation.DoesNotExist:
                return Message.objects.none()

            if user not in conversation.participants.all():
                raise PermissionDenied("You are not a participant of this conversation.")

            return Message.objects.filter(conversation=conversation)

        # Optionally restrict to all user messages
        return Message.objects.filter(conversation__participants=user)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return MessageCreateSerializer
        return MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
