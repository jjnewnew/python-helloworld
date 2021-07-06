# Install minimal Python 3.
FROM python:3.9-alpine
# Copy app source code.
COPY . /app
WORKDIR /app
# Install Python requirements.
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]
