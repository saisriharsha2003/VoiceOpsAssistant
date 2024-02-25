from virtual_assistant import desktop_assistant, speak, inputCommand, user
from googlesearch import search
import webbrowser as wb

def chrome_search():
    print(desktop_assistant + ": what should i search for you sir?")
    speak("what should i search for you sir?")
    chrome_query = inputCommand()
    print(user + ": " + chrome_query)
    res = "searching" + chrome_query + " for you sir...."
    print(desktop_assistant + ": " + res)
    speak(res)
    search_results = search(chrome_query, num_results=1)
    first_result = next(search_results, None)
    if first_result:
        wb.open(first_result)