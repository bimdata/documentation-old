FROM python:3.7
WORKDIR /opt
ADD doc_sphinx/requirements.txt /opt
RUN pip install -r requirements.txt
COPY ./ /opt
RUN git remote set-url origin https://github.com/bimdata/documentation.git && sphinx-versioning build doc_sphinx html_doc

FROM nginx:stable-alpine
COPY --from=0 /opt/html_doc/ /usr/share/nginx/html/
COPY --from=0 /opt/redoc/ /usr/share/nginx/html/redoc/
