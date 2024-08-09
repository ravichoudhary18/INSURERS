FROM node:18-alpine
WORKDIR /frontend
RUN npm install vite
COPY package.json .
RUN npm install
COPY . .
CMD npm run dev