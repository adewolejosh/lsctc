FROM node:12

WORKDIR /lsctc-js-server

COPY package.json /lsctc-js-server

RUN npm install

COPY . /lsctc-js-server

EXPOSE 3000

CMD ["npm", "start"]
