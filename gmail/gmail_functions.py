import base64
import email
from gmail.gmail_service import user_id
from gmail.gmail_message import ListMessagesMatchingQuery, GetMessage


def get_stamped_mime_messages(sender, service):
    msgs = list_messages(sender, service=service)
    if len(msgs) == 0:
        return []

    msgs_content = GetMessage(service=service, user_id=user_id,
                              msg_ids=[m['id'] for m in msgs],
                              format="raw"
                              )

    print("Mime", len(msgs_content))
    mime_msgs = []
    for m in msgs_content:
        msg_str = base64.urlsafe_b64decode(m['raw'].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_str)

        mime_msgs.append(mime_msg)
    return mime_msgs


def listen_and_deliver(sender, destination, service):
    msgs = get_stamped_mime_messages(sender, service=service)
    for m in msgs:
        m['To'] = destination
        message = {'raw': base64.urlsafe_b64encode(m.as_bytes()).decode()}
        message_ = service.users().messages().send(userId=user_id, body=message).execute()
        print(message_)
    print("Done")


def list_messages(sender, service):
    query = "from:{}".format(sender)
    mmm = ListMessagesMatchingQuery(
        service=service,
        user_id=user_id,
        q=query
    )
    print("ListMsg", len(mmm))
    return mmm
