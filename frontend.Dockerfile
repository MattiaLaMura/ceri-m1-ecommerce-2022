# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY ./frontend/vue-project/package*.json ./
RUN npm install
COPY ./frontend/vue-project .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/
EXPOSE 1111

CMD ["nginx", "-g", "daemon off;"]
