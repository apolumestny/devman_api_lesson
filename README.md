# Bitly url shorterer

this script gets the URL as an argument. If ULR is bitlink script return count of click, otherwise return shortened URL

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
set in .env variable GET_ACCESS_TOKEN equal to access token you got in the self-care cabinet.

### How to use
to shorten the link use 
```
python main.py https://stackoverflow.com/questions/
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
