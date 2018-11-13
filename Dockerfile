FROM python:3.7
WORKDIR /opt
ADD doc_sphinx/requirements.txt /opt
RUN pip install -r requirements.txt
COPY ./ /opt
RUN mkdir ~/.ssh && echo "$SSH_KEY" > ~/.ssh/id_rsa && ~/.sphinx-versioning build doc_sphinx ../html_doc && rm -rf ~/.ssh

FROM nginx:stable-alpine
COPY --from=0 /opt/html_doc/ /usr/share/nginx/html/
COPY --from=0 /opt/redoc/ /usr/share/nginx/html/redoc/
