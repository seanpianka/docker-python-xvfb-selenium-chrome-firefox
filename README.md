# docker-python-xvfb-chromium-selenium

Dockerfiles for images running Python 2.7 or Python 3.6 + Selenium with either Chrome or Firefox and using Xvfb for the X display (necessary for running Selenium headlessly).

## Dependencies

 - Python 2.7 or Python 3.6
 - Google Chrome/Chromium or Firefox (Unstable, from Debian)
 - Chromedriver or Geckodriver
 - Selenium
 - Xvfb

## Usage Tutorial

##### Your Project Files
A project directory under `/opt/app/` is created within the Docker image. This is where all of your project files will be copied over (`/opt/app/` is a common convention). Create a new file (this will be our project file for this tutorial) using `$ touch test.py`. We'll write our application in this file, see below:

    from selenium import webdriver
    
    # use selenium, instantiate Chrome browser instance
    options = webdriver.chrome.options.Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(chrome_options=options)
    
    # perform a test request to verify that selenium and chrome are working properly
    driver.get("https://httpstat.us/200")
    if "200 OK" in driver.page_source:
        print('Selenium successfully opened with Chrome (under the Xvfb display) and navigated to "https://httpstat.us/200", you\'re all set!')

##### Your Project's Entry Point
Then, modify the invocation shell script `run.sh` ([AVAILABLE HERE](https://github.com/seanpianka/docker-python-xvfb-selenium-chrome-firefox/blob/master/py3/chrome/run.sh)) and ensure the last line contains the correct Python invocation of the entry point into your application. This script is what the Dockerfile will use, along with Bash, to invoke the Python interpreter on the entry point you specify.

    python3 test.py  # change this line to invoke the entry point of your application!

##### Dockerfile Explanation and Build Steps
Now, we're going to build and run our project! Yay! Start by modifying the `Dockerfile` ([AVAILABLE HERE](https://github.com/seanpianka/docker-python-xvfb-selenium-chrome-firefox/blob/master/py3/chrome/Dockerfile)) for Python 3 + Chrome. 

First, the Dockerfile installs chromium, Xvfb, and Python. Then, a project directory is created, the Python project dependencies (and Selenium) are installed, and your project code is copied into the image. Lastly, env `DISPLAY` is set to an open display port for Xvfb to use (as we require an X Windows server), your invocation script `run.sh` ([AVAILABLE HERE](https://github.com/seanpianka/docker-python-xvfb-selenium-chrome-firefox/blob/master/py3/chrome/run.sh)) is copied into the image and invoked with `/bin/bash`.

Now, build the image and spawn a new container using that image:

    $ docker build -t docker-python-xvfb-selenium-chrome-firefox .
    
##### Executing Your Project
Now, create a new container from your image:

    $ docker run --rm docker-python-xvfb-selenium-chrome-firefox
    
You should see the following text output to the terminal:

>Selenium successfully opened with Chrome (under the Xvfb display) and navigated to "https://httpstat.us/200", you're all set!

##### Done!

Pre-written Dockerfiles for any combination of Python 2/Python 3 and Chrome/Firefox are available! 
