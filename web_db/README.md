# Restful-api-example
simple restful web app


# To run this project in docker:
 - git clone <Restful-api-example>
 - cd Restful-api-example/web_db
 - docker build .
 - docker run -p 8099:8099 <image>

Then in http://127.0.0.1:8099 you can see simple web app.
After testing this app you can delete docker image and container.


# To run this project in virtualenv:
 - git clone <Restful-api-example>
 - python3 -m venv env
 - source env/bin/activate
 - cd Restful-api-example/web_db
 - pip install -r requirements.txt
 - python main.py

Then in http://127.0.0.1:8099 you can see simple web app.
After testing this app you can exec: 
 - deactivate
 - cd ..
 - rm -rf env
