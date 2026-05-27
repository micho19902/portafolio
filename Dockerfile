# Usa una imagen oficial de Python
FROM python:3.12

# --- Configuración para Render ---
# Render asigna el puerto a través de esta variable de entorno
ARG PORT=10000
# Necesitamos construir la app con la URL de tu futuro despliegue
ARG API_URL=https://portafolio.onrender.com
ENV PORT=$PORT API_URL=$API_URL

# Instala el servidor web Caddy para servir el frontend
RUN apt-get update -y && apt-get install -y caddy && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Crea un archivo de configuración para Caddy
# Este actúa como un "proxy inverso" para dirigir el tráfico
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

# Copia el contenido de tu proyecto al contenedor
COPY . .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# --- Este es el proceso de construcción de Reflex ---
# Inicializa la app
RUN reflex init

# Exporta el frontend (los archivos HTML, CSS, JS) y los mueve a donde Caddy pueda verlos
RUN reflex export --frontend-only --no-zip && mv .web/_static/* /srv/ && rm -rf .web

# Expone el puerto que usará Render
EXPOSE $PORT

# Comando para iniciar la aplicación en modo producción
# Esto inicia Caddy (el servidor web) y luego el backend de Reflex
CMD caddy start && reflex run --env prod --backend-only --loglevel debug