FROM node:lts-alpine

WORKDIR /dcfront

#COPY package*.json ./
#
#RUN npm install

COPY . .

COPY package*.json ./

RUN npm install

#COPY package.json /dcfront/package.json
#
#RUN npm install

EXPOSE 8001
