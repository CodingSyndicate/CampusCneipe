# Build Stage 1
# This build created a staging docker image
#
FROM node:16.5.0 as build

WORKDIR /frontend

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build


# Build Stage 2
# This build takes the production build from staging build
#
FROM nginx:stable

RUN rm -rf /usr/share/nginx/html && mkdir /usr/share/nginx/html
COPY --from=build /frontend/build /usr/share/nginx/html