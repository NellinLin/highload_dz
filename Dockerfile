FROM python:3.7.2-alpine3.8
LABEL maintainer="NellinLin"
RUN apk update && apk upgrade && apk add bash
COPY . ./highload
EXPOSE 81
WORKDIR ./highload
CMD ["python3", "./server.py"]
