# Here we will try to launch a browser with a specified URL 
import webbrowser, time, pyautogui
import random
import requests

# # Here we pass the link to open in a variable
# query = "python"

# # Here is the URL after adding the query 
# finalUrl = ("https://www.bing.com/search?q=" + query)



# # Since, Edge is my default browser, it is opening EDGE
# webbrowser.open(finalUrl)
# time.sleep(4)
# pyautogui.hotkey("ctrl","w")

# print("Job done!")

# A function to get random words, got from internet


def get_list_of_words():
    response = requests.get(
        'https://www.mit.edu/~ecprice/wordlist.10000',
        timeout=10
    )

    string_of_words = response.content.decode('utf-8')

    words = string_of_words.splitlines()

    # words = get_list_of_words()
    # print(words)

    random_word = random.choice(words)
    print(random_word)  # 👉️ zoo

    url = ("https://www.bing.com/search?q=" + random_word)

    webbrowser.open(url)
    time.sleep(3)
    pyautogui.hotkey("ctrl","w")


# Now we have to make the searching part in a Function 

# def search():
#     # query = "random things here"
#     url = ("https://www.bing.com/search?q=" + random_word)

#     webbrowser.open(url)
#     time.sleep(3)
#     pyautogui.hotkey("ctrl","w")

#     print(url)

for _ in range(3):
    get_list_of_words()
    # search()
    



# Next we need to make a List of search terms to Loop through 

# With every iteration of the Loop, the value will be stored and passed to the search function