import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                '< Micho /', rx.text.strong(' DEVOPS ', color="#0558be"), '>'
            ),
            rx.hstack(            # 👈 Envolvemos momento y color_mode
                rx.moment(interval=1000, format='YYYY/MM/DD HH:mm:ss'),
                rx.color_mode.button(),
                spacing="4",      # espacio entre ambos
                align="center",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        margin_bottom="20px",
    )