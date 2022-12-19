FROM node:19

## Buiiding application
# Create a directory /app and cd into it
WORKDIR /app

ADD main.js .
ADD package.json .
ADD package-lock.json .
ADD views views
ADD public public

# Install node modules
RUN npm ci 

## Run Application
# Set PORT to 3000
ENV PORT=3000 
ENV INSTANCE_NAME=""
ENV INSTANCE_HASH=""
# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
CMD curl -s http://localhost:${PORT}/health || exit 1


# What port does the application binds to
EXPOSE ${PORT}
ENTRYPOINT node main.js

# docker build -t nicholaslimgt/cfdsa-fortune:1.0.0

## how to run application
# docker run -d -p 8080:3000 --name fortune nicholaslimgt/cfdsa-fortune:1.0.0

## to do inspection
# docker inspect <tag> 

## Additional notes
# standard commands will not work if base image does not have a shell
# will need to use docker commands to do so
# eg instead of ENTRYPOINT node main.js
# have to use 
# ENTRYPOINT ["node"]
# CMD ["main.js"]