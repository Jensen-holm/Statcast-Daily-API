# Statcast-Daily-API
API called by the RealTimeMLB application to retrieve the most up to date ball physics metrics. <br>
Note that docker instructions could be different depending on your OS, I am running Ubuntu.

## Install

1. `git clone https://github.com:Jensen-holm/Statcast-Daily-API.git`
2. `cd Statcast-Daily-API.git`

## Docker Build & Run 

(on my machine, I called the image name statcast-daily) <br>
3. `sudo docker build -t [imagename] .` 
4. `sudo docker run [imagename] --network="host"`


## Venv Install and Run

3. `virturalenv venv`
4. `source venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. `python3 app.py`


