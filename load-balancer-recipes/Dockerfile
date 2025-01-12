FROM nginx:1.27.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV AM_I_IN_A_DOCKER_CONTAINER Yes

RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf  /etc/nginx/conf.d/default.conf