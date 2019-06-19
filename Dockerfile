FROM python:3.7

RUN wget https://raw.githubusercontent.com/visionmedia/n/master/bin/n -O /usr/local/bin/n && \
    chmod +x /usr/local/bin/n && \
	n 10

WORKDIR /opt
ADD doc_sphinx/requirements.txt /opt
RUN pip install -r requirements.txt

ADD doc_sphinx/package.json /opt
ADD doc_sphinx/package-lock.json /opt
RUN npm ci

ARG API_URL
ARG CDN_URL
ARG CONNECT_URL
ARG PLAYGROUND_CLIENT_ID
ARG WHITELIST_BRANCHES

ENV API_URL=$API_URL
ENV CDN_URL=$CDN_URL
ENV CONNECT_URL=$CONNECT_URL
ENV PLAYGROUND_CLIENT_ID=$PLAYGROUND_CLIENT_ID
ENV WHITELIST_BRANCHES=$WHITELIST_BRANCHES

COPY ./ /opt
RUN mv /opt/node_modules /opt/doc_sphinx/node_modules

RUN sphinx-build doc_sphinx html_doc

FROM nginx:stable-alpine
COPY --from=0 /opt/html_doc/ /usr/share/nginx/html/
COPY --from=0 /opt/redoc/ /usr/share/nginx/html/redoc/
