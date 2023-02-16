# messenger-proxy-bot

## Description
**messenger-proxy-bot** is a comprehensive messenger chatbot utility that provides an interface to various web information sources on the messenger platform. Users may interact with a bot user in CLI form, retrieving data in the form of plain text.

### Motivation
The project is the solution to a problem faced by frqeuent flyers: **rate limitations on in-flight wifi**. While many airlines today provide free in-flight wifi, usage is often limited to siple messaging apps (such as Meta's Messenger), leaving those wanting to search the broader web with no solution other than to text loved ones which are not onboard. **messenger-proxy-bot** provides all these utilities while putting no more strain on the in-flight network than what is normally allowed by setting up a local system that relays search requests and returns them in the form of chat messages. 

### Currently supported interfaces
- Google search
- Wikipedia 
- ChatGPT

## Setup
- Clone this repository
- Rename `sample.env` to `.env`, entering login credentials for your messenger bot
- Follow the installation guide on [chatGPT-wrapper](https://github.com/mmabrouk/chatgpt-wrapper) to setup chatGPT interface utility
- Run `py proxybot.py` to launch the program, which will listen to user requests indefinitely until terminated

## Usage
- `help`: lists all possible commands
- `google <keyword>`: get Google search results
- `wiki(pedia) [-f] <keyword>`: get Wikipedia page summary (-f for full article)