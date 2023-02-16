import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import wikipedia

CHUNK_LEN = 10000
def chunk_string(input_string, chunk_len):
    return [input_string[i : i + chunk_len] for i in range(0, len(input_string), chunk_len)]

def make_google_query(query_string):
    # Get query source
    query = urllib.parse.quote_plus(query_string)
    session = HTMLSession()

    # Make query
    response = session.get("https://www.google.com/search?q=" + query)
    
    # Parse results
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)
    
    # Format output
    formatted_output_str = ""
    count = 1
    for result in results:
        try: 
            item_title = result.find(css_identifier_title, first=True).text
            item_link = result.find(css_identifier_link, first=True).attrs['href']
            item_text = result.find(css_identifier_text, first=True).text
            
            formatted_output_str += f"{count}. {item_title}\n{item_text}\n({item_link})\n------------\n\n"
            count += 1
        except:
            pass

    return formatted_output_str

def make_wikipedia_query(query_string, full_length = False):
    # Make wikipedia search query for title
    wiki_query = wikipedia.search(query_string, results = 1, suggestion= False)

    # No title found
    if not wiki_query:
        return "Article not found, please try again"
    
    # Return summary or full text of article requested
    if full_length:
        return wikipedia.page(wiki_query[0], auto_suggest= False).content
    return wikipedia.page(wiki_query[0], auto_suggest= False).summary

def gen_response(request_command):
    try:
        if request_command == "" :
            return []
        request_list = request_command.split()
        q_command = request_list[0].lower()
        if q_command == "help":
            return ["""Possible commands:\n\n
            - `google <keyword>` : get Google search results\n\n
            - `wiki(pedia) [-f] <keyword>` : get Wikipedia summary (-f for full article)"""]
        if q_command == "google":
            google_result = make_google_query(' '.join(request_list[1:]))
            return chunk_string(google_result, CHUNK_LEN)
        if q_command == "wiki" or q_command == "wikipedia":
            if request_list[1].lower() == "-f":
                wiki_result = make_wikipedia_query(' '.join(request_list[2:]), full_length = True)
            else:
                wiki_result = make_wikipedia_query(' '.join(request_list[1:]))
            return chunk_string(wiki_result, CHUNK_LEN)
    except:
        return ["An internal error occurred. Please try again later."]
    return ["Unknown command. Type \'help\' to get a list of commands."]
