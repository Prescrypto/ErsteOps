from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    def __str__(self):
        return self.label

@python_2_unicode_compatible
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')
    
    def as_dict(self):
        return {'handle': self.handle, 'message': self.message,
                'timestamp': self.formatted_timestamp}

'''
import json
from channels import Group
@python_2_unicode_compatible
class Room(models.Model):
    title = models.CharField(max_length=255)
    staff_only = models.BooleanField(default=False)
    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)
    def send_message(self, message, user):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message,
                'username': user.username}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )

    def __str__(self):
        return self.title
'''