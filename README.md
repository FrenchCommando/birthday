# Birthday

- build the `credential.json` from this link
`https://developers.google.com/gmail/api/quickstart/python`

- run `gmail_service.py` to generate `token.pickle` from `credentials.json`


- make changes in `gmail_main.py`
    - `sender` is the address from which you want to forward emails
    - `destination` is the address you want to forward to
```python
def main():
    service = load_creds()
    sender = "noreply@metmuseum.org"
    destination = "mail@frenchcommando.com"
    # forwards all emails from {sender} to {destination}
    listen_and_deliver(sender, destination, service)


if __name__ == '__main__':
    main()
```

# Acknowledgement

- this is a nice cheatsheet: `https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet`
- this is the other projected from which I pulled all the code `https://github.com/FrenchCommando/gmail-forwarding`
