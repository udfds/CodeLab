https://hub.docker.com/r/ppodgorsek/robot-framework


docker run -v ${PWD}/reports:/opt/robotframework/reports:Z -v ${PWD}/test/draft/:/opt/robotframework/tests:Z -e BROWSER=chrome ppodgorsek/robot-framework:latest
    