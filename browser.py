# Here we will try to launch a browser with a specified URL 
import webbrowser, time, pyautogui

# Here we pass the link to open in a variable
query = "python"

# Here is the URL after adding the query 
finalUrl = ("https://www.bing.com/search?q=" + query)



# Since, Edge is my default browser, it is opening EDGE
webbrowser.open(finalUrl)
time.sleep(4)
pyautogui.hotkey("ctrl","w")

print("Job done!")


# Now we have to make the searching part in a Function 

# Next we need to make a List of search terms to Loop through 

# With every iteration of the Loop, the value will be stored and passed to the search function