FROM python:3.12-slim

# Variable de entorno para el puerto que Render asigna
ARG PORT=10000
ENV PORT=$PORT
ENV PYTHONUNBUFFERED=1

# Instalar Caddy y Node.js
RUN apt-get update -y && apt-get install -y caddy curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Configuración de Caddy (el proxy inverso)
RUN cat > Caddyfile <<EOF
:${PORT}

encode gzip

@backend_routes path /_event/* /ping /_upload/* /_upload
handle @backend_routes {
	reverse_proxy localhost:8000
}

root * /srv
route {
	try_files {path} {path}/ /index.html
	file_server
}
EOF

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Inicializar Reflex
RUN reflex init

# Exportar frontend estático y moverlo donde Caddy lo encuentra
RUN reflex export --frontend-only --no-zip && \
    mkdir -p /srv && \
    cp -r .web/_static/* /srv/ && \
    rm -rf .web

EXPOSE $PORT

# Comando de inicio: Caddy + backend de Reflex
CMD caddy start && reflex run --env prod --backend-only --loglevel warn