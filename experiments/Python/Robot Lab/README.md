
#### Docker used
    - https://hub.docker.com/r/ppodgorsek/robot-framework

#### Runnig tests in Docker (command line)
    - docker run -v ${PWD}/reports:/opt/robotframework/reports:Z -v ${PWD}/tests/suite_draft/:/opt/robotframework/tests:Z -e BROWSER=chrome ppodgorsek/robot-framework:latest

#### Record page
    - https://chrome.google.com/webstore/detail/robotcorder/ifiilbfgcemdapeibjfohnfpfmfblmpd

#### Running tests in local (command line)
    - robot /tests/suite_draft/tc_0xy.robot

#### VSCode extensions
    - RobotF Extension
    - Robot Framework Intellisense

#### VSCode configuration
    - File > Preferences > Settings
        - Type: 'format on save'
        - Check the feature (Restart the VSCode)
