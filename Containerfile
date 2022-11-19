FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN ailab create-db
RUN ailab populate-db
RUN ailab add-user -u admin -p admin
EXPOSE 5000
CMD ["ailab", "run"]
