import setup_environment, urbanairship
from server.models import User, Notification

# Obtain all notifications that are not done.
notif_list=Notification.objects.filter(done=False)

# Setup urban airship
airship = urbanairship.Airship('EkqcG1DpQcWBgekENCBSYw',
			       			   '9U1SqeG1TuasAfVR4UNc9w')

for notif in notif_list:
  # Obtain user and device token
  user = User.objects.get(user_id=notif.user_id)
  device_token = user.device_token
  # Push notification
  airship.push({'aps': {'alert': notif.notification}},
                device_tokens=[device_token],
		schedule_for=str(notif.schedule_time))
  # Mark the notification as done
  notif.done = True
  notif.save()
