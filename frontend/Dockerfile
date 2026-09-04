FROM node:26-slim

WORKDIR /app

COPY package*.json ./
RUN npm install --ignore-scripts

COPY . .

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]