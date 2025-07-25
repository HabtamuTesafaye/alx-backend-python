import time
from datetime import datetime
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import logging
from collections import defaultdict
from threading import Lock

# Set up logger for requests
logger = logging.getLogger('request_logger')
handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Thread-safe store for tracking messages by IP
message_counts = defaultdict(list)
lock = Lock()

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_msg = f"{datetime.now()} - User: {user} - Path: {request.path}"
        logger.info(log_msg)


class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_hour = datetime.now().hour
        # Allow access only between 6AM and 9PM (6 <= hour < 21)
        if current_hour < 6 or current_hour >= 21:
            return HttpResponseForbidden("Access to chat is restricted between 9PM and 6AM.")


class OffensiveLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == "POST" and request.path.startswith('/api/messages/'):  # adjust path to your messages endpoint
            ip = self.get_client_ip(request)
            now = time.time()

            with lock:
                # Clear timestamps older than 60 seconds
                message_counts[ip] = [t for t in message_counts[ip] if now - t < 60]

                if len(message_counts[ip]) >= 5:
                    return HttpResponseForbidden("Too many messages sent. Please wait before sending more.")
                
                # Record this message timestamp
                message_counts[ip].append(now)

    def get_client_ip(self, request):
        # Common way to get real IP behind proxies
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class RolePermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Example: restrict PUT, PATCH, DELETE to admin/moderator only
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            user = request.user
            if not user.is_authenticated:
                return HttpResponseForbidden("Authentication required.")
            # Assuming your User model has a 'role' field
            if getattr(user, 'role', None) not in ['admin', 'moderator']:
                return HttpResponseForbidden("You do not have permission to perform this action.")
