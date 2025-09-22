# Installation
Follow these steps first if you are running the app on your local machine or on docker:
- Download the Google Cloud Vision service account credentials file
- Rename the file to `service-account.json` or update the reference in docker-compose file
- Store the file in the root directory of this project

Create a virtual env for python
```shell
python3 -m venv venv
```
install the required packages
```shell
pip install -r requirements.txt
```

Export the Google Cloud credentials and Flask app entry point
```shell
export GOOGLE_APPLICATION_CREDENTIALS='path/to/your/service-account-key.json'
export FLASK_APP=wsgi.py
```

Run the application
```shell
flask run
```
This will start the application in port `5000` of localhost.

## Setup with Docker

If you have stored the service-account credentials file in the root directory of this application, then you can directly run the following command to build & start the application. Otherwise you have to update the credentials file reference in the docker-compose file and then run this command.

```shell
docker-compose up --build
```

To stop the application, run the following command.
```shell
docker-compose down
```

## Curl Examples

**Note:** If you have started the application with docker, then you will need to update the port from `5000` to `8080` for the following APIs.

/extract-text
```shell
curl --location 'localhost:5000/api/v1/extract-text' \
--form 'file=@"your-image-file-path-here"'
```