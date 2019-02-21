FROM python:3.7
WORKDIR /opt
ADD doc_sphinx/requirements.txt /opt
RUN pip install -r requirements.txt

ADD doc_sphinx/package.json /opt
ADD doc_sphinx/package-lock.json /opt
RUN cd doc_sphinx && npm ci

ARG API_URL
ARG CDN_URL
ARG CONNECT_URL
ARG WHITELIST_BRANCHES

ENV API_URL=$API_URL
ENV CDN_URL=$CDN_URL
ENV CONNECT_URL=$CONNECT_URL
ENV WHITELIST_BRANCHES=$WHITELIST_BRANCHES

COPY ./ /opt
RUN git remote set-url origin https://github.com/bimdata/documentation.git && sphinx-versioning build doc_sphinx html_doc

FROM nginx:stable-alpine
COPY --from=0 /opt/html_doc/ /usr/share/nginx/html/
COPY --from=0 /opt/redoc/ /usr/share/nginx/html/redoc/
