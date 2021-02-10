from gmail.gmail_service import load_creds
from gmail.gmail_functions import listen_and_deliver


def main():
    service = load_creds()
    sender = "noreply@metmuseum.org"
    destination = "mail@frenchcommando.com"
    # forwards all emails from {sender} to {destination}
    listen_and_deliver(sender, destination, service)


if __name__ == '__main__':
    main()
