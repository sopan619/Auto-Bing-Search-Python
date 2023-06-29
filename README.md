# Automated Microsoft Reward Script
## **Please note that this might get you banned. Use at your own Risk and Discretion!!**
### **I am using it for some time, so far so good.**

<img src="https://img.freepik.com/free-icon/snakes_318-368381.jpg" width="80" height="80">

### This is a simple Python program I made for myself to save some repetitive steps on a daily basis.
## This is a simple script that,
* Opens the **Default Browser** of your system.
* Performs the set number of searches on Bing website.
* Gets you daily points with 1 simple click.

To use this script, you need to have Python installed on your system.
## You can [Download Python](https://www.python.org/downloads/) from here.
### Next you want to install the Modules reqired.
Simple open the terminal and run following commands.

`pip install requests`

`pip install pyautogui`

### That's all, you can now run the python file and it will do the search for you.
You can open a Terminal at the file location, then run the following command,
```
python broswer.py
```

## Changes 29th June'23
+ Now the program will ask for the number of searches you wish to perform before executing. Simply enter the value and start.
+ Added a random search delay between 3 to 12 seconds, you can change it by editing the code or just let it be. Did it in hopes to avoid ban! Not sure if it will help.

## Notes
* Make sure to set **Microsoft Edge as your Default Browser**. Else it will open in Chrome or whichever is your Default Browser.
* If you use Chrome, then you must be logged in there with your Microsoft Account in order to earn the points.
* Note, the next part has been changed to generate a random delay every time, you change it by commenting out the random function and add your own delay number as shown below.
* You can set/change the amount of time a tab is kept opened by changing the following line in the code file,
  ```python 
  # After the set amount of time, the next line will be executed, and browser window will be closed
    time.sleep(3)
  ```
  Simply change the number of seconds you want the tab to be opened. Here it is set to 3 seconds, which works for me.
* The next part is not necessary anymore, but for record I am leaving it here anyways.
* To change the number of searches, you change the following line,
  ```python
  for _ in range(3): 
    searchAuto()
  ```
  Simply change the range value to desired number of searches. Here in the example it is set to 3 searches.

  ## Thank you for checking out my code, I am a beginner in this world of coding, I know this can be imporoved, as I also imporve I will update this program as well.
  #Have fun!
