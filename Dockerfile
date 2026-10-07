FROM nginxinc/nginx-unprivileged:1.29-alpine

COPY src/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
