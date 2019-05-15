Docker with Pyspark

Container ubuntu w/Pyspark config
===============
- name: cocky_leavitt
- container_id: 17a1824840be
- docker start cocky_leavitt
- docker stop cocky_leavitt
- docker exec -it 17a1824840be /bin/bash

port 7077
============
- It's the Master Node for the pyspark service
- In charge of delegating work to slaves
- It's the port for Input Jobs
- We do not interact directly with this port

port 4040
============
- Slave/Worker Node
- It's the UI for PySpark Jobs


It is recommended to use Gunicorn to as a web server
https://www.google.com/search?q=gunicorn&oq=guni&aqs=chrome.1.69i57j0l5.5472j0j1&sourceid=chrome&ie=UTF-8


