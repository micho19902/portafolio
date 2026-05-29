import reflex as rx

config = rx.Config(
    app_name="portafolio",
    # frontend_port=10000,   # El puerto que Render espera para el frontend
    # backend_port=8000,     # El puerto interno del backend (no lo expone Render)
    api_url="http://localhost:8000", 
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)