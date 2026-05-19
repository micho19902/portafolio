import reflex as rx



def aboutMy() -> rx.Component:
    return rx.scroll_area(
        rx.text(
            'Con más de 15 años de experiencia en el mundo de TI, mi carrera ha recorrido desde la administración de sistemas, redes y soporte, hasta el aseguramiento de la calidad y el despliegue de infraestructuras. He construido mi camino sobre una base sólida de tecnologías como Docker, Ansible, Prometheus (nivel básico), Linux (mi gran pasión, hoy con Arch Linux), scripting en Bash/Python, y una amplia experiencia en entornos de virtualización con esXi, Proxmox y VMware, además de bases de datos como Oracle y PostgreSQL.'
        ),
        type='hover',
        height='90px',
        margin='4px',
        # height='auto|auto',
        # bg="#4D4848",
        # width='auto|auto'
        # border='2px solid white',
        # border_radius='10px'
    )