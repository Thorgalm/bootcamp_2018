import requests

# resp = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")

# text = resp.content.decode()
# print(text)

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}"

# nothing = "12345"
nothing = "8022"
i = 0
while True:
    i += 1
    x_url = url.format(nothing)
    resp = requests.get(x_url)
    print(i, x_url)
    try:
        nothing = int(resp.text.split()[-1])
    except ValueError:
        print(resp.text)
        break

# peak.html
# view-source:http://www.pythonchallenge.com/pc/def/peak.html
# http://www.pythonchallenge.com/pc/def/pickle.html