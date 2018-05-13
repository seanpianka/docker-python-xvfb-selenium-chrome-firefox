# docker-python-xvfb-chromium-selenium

Dockerfile for an image with Python and a functional Selenium or Chrome/Firefox installation with Xvfb for the X display (necessary for running Selenium headless).

## Includes:

 - Python 2 or Python 3
 - Google Chrome/Chromium or Firefox (Unstable, from Debian)
 - Chromedriver or Geckodriver
 - Selenium
 - Xvfb

## Usage:

A project directory under `/opt/app/` is created within the Docker image and is where all files will be copied over to by convention (feel free to change this, but this is a common convention). 

Below are (hopefully) complete descriptions of how to both copy all your project files and install your project's Python dependencies into the Docker image.

The Docker image is built with:

`docker build -t project-tag-name .`

The Docker image is made into a container and run with:

`docker run project-tag-name`

Optionally, you can use `docker run`'s `--rm` flag to remove the container after the container has exited. I find this useful for testing and debugging the container during development.

## How-To:

Below are sections describe how to modify `Dockerfile` to work for your individual project. There are two sections, one for **Chrome** and one for **Firefox**: the instructions are _fundamentally identical_, however line numbers have been changed within the instructions for the different `Dockerfile`s necessary for each browser.

A convention for describing a specific line within a specific file is `filename:#` where `filename` is the file to be viewed and `#` is the line-number which should be viewed.

### Include Project Files
#### Top-level files
##### Chrome

There is a `COPY` command on `Dockerfile:24` which will copy any top level files required for your project into the Docker image's project directory under `/opt/app/`. Replace `test.py` and include a space-separated list of files to be copied over, ensuring the last argument to `COPY` is `.` (so that the files are copied over to `/opt/app`.

##### Firefox

There is a `COPY` command on `Dockerfile:29` which will copy any top level files required for your project into the Docker image's project directory under `/opt/app/`. Replace `test.py` and include a space-separated list of files to be copied over, ensuring the last argument to `COPY` is `.` (so that the files are copied over to `/opt/app`.

#### Modules and Other Sub-Directories
##### Chrome

There is a `COPY` command on `Dockerfile:22` which will copy the sub-directories required for your project into the Docker image's project directory under `/opt/app/`. Replace `app/` and include a space-separated list of directories to be copied over, ensuring the last argument to `COPY` is `.` (so that the directories are copied over to `/opt/app`.

##### Firefox

There is a `COPY` command on `Dockerfile:27` which will copy the sub-directories required for your project into the Docker image's project directory under `/opt/app/`. Replace `app/` and include a space-separated list of directories to be copied over, ensuring the last argument to `COPY` is `.` (so that the directories are copied over to `/opt/app`.

### Installation of Project Dependencies
#### In-line Installation
##### Chrome

Modify Python project dependencies inline within `Dockerfile` by adding the package names to the arguments of the `pip3 install ...` command on `Dockerfile:28`.

##### Firefox

Modify Python project dependencies inline within `Dockerfile` by adding the package names to the arguments of the `pip3 install ...` command on `Dockerfile:33`.

#### File `requirements.txt` Installation

##### Chrome

Commenting out (remove) `Dockerfile:28` and uncomment in (include) `Dockerfile:30-31` to copy over your `requirements.txt` and install the packages listed to your Docker image's Python environment.

##### Firefox

Commenting out (remove) `Dockerfile:33` and uncomment in (include) `Dockerfile:35-36` to copy over your `requirements.txt` and install the packages listed to your Docker image's Python environment.

## Tests:

Clone and enter the repository:

`$ git clone https://github.com/seanpianka/docker-python-xvfb-selenium-chrome-firefox`

`$ cd docker-python-xvfb-selenium-chrome-firefox/py#/browser/` 

<sup>Make sure to replace `py#` with a Python version to use and `browser` with a browser to use.</sup>

Build the Docker image:

`$ docker build -t docker-python-xvfb-selenium-chrome-firefox .`

Run the Docker image (and delete after it has completed):

`$ docker run --rm docker-python-xvfb-selenium-chrome-firefox`

The output (to stdout) of this container after successful execution should be the following:

> Selenium successfully opened with {your browser} (under the Xvfb display) and navigated to "https://httpstat.us/200", you're all set!

If you see the above output, you're good to go with the further development of your project!

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
