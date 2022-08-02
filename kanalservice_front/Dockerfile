FROM node
WORKDIR /usr/src/app/front
COPY package.json /usr/src/app/front/package.json
RUN npm install
RUN npm install react-script

COPY ./entrypoint-front.sh /usr/src/app/front/
RUN chmod +x /usr/src/app/front/entrypoint-front.sh


COPY . /usr/src/app/front
