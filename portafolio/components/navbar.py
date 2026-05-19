import reflex as rx



def navbar() -> rx.Component:
    return rx.box(
        rx.text(
            '< Micho /', rx.text.strong(' DEVOPS ', color="#0558be"), '>'
            
        ),
        # rx.image(src=)
        rx.color_mode.button(position='top-right'),
        margin_bottom='20px'

    )