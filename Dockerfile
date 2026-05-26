# This Dockerfile is used to deploy a single-container Reflex app instance
# to services like Render, Railway, Heroku, GCP, and others.

# It uses a reverse proxy (Caddy) to serve the frontend statically and proxy to backend
# from a single exposed port.
FROM python:3.12

# Render espera el puerto 10000, pero lo toma de la variable de entorno $PORT
ARG PORT=8080
ARG API_URL
ENV PORT=$PORT API_URL=${API_URL:-http://localhost:$PORT}

# Instalar Caddy server (reverse proxy) dentro de la imagen
RUN apt-get update -y && apt-get install -y caddy && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Crear archivo de configuración de Caddy para que sirva como proxy inverso
RUN cat > Caddyfile <<EOF
:{\$PORT}

encode gzip

@backend_routes path /_event/* /ping /_upload /_upload/*
handle @backend_routes {
	reverse_proxy localhost:8000
}

root * /srv
route {
	try_files {path} {path}/ /404.html
	file_server
}
EOF

# Copiar todo el código al contenedor
COPY . .

# Instalar dependencias de Python
RUN pip install -r requirements.txt

# Inicializar Reflex y preparar la app
RUN reflex init

# Exportar el frontend como archivos estáticos y moverlos a /srv
RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web

# Necesario hasta que Reflex maneje correctamente SIGTERM
STOPSIGNAL SIGKILL

EXPOSE $PORT

# Comando para iniciar la aplicación
CMD [ -d alembic ] && reflex db migrate; \
    caddy start && reflex run --env prod --backend-only --loglevel debug