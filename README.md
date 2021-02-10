# Birthday

## Email part

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

## Webpage part

Here is where I found the tutorial for `aiohttp` with html templates:
`https://us-pycon-2019-tutorial.readthedocs.io/aiohttp_templates_full.html`

- Put the name of your significant other there in `host_page.py`
```python
    context = {
        "username": "My Darling",
    }
```

- put whatever port number you want the page to be hosted on
```python
web.run_app(init_app(), port="8888")
```

- move `token.pickle` generated from previous step in the project folder (or play around with the paths in the project)
- run `host_page.py`

Personnaly I use `nginx` to manage the domains and load-balancing. (I guess that's what most people do)

# Acknowledgement

- this is a nice cheatsheet: `https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet`
- this is the other projected from which I pulled all the code `https://github.com/FrenchCommando/gmail-forwarding`
