FROM node:16-alpine

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build

EXPOSE 8001
ENV PORT=8001 
CMD ["node", "build/index.js"]