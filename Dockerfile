# Pull Images
FROM python:3.7.5-alpine

# Dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Work Directory
WORKDIR /usr/src/app

# Requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy files
COPY . .

# Run project
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "src.app:app" ]

# Expose Port
EXPOSE 5000