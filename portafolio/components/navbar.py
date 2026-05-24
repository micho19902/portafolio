import reflex as rx



def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
        rx.text(
            '< Micho /', rx.text.strong(' DEVOPS ', color="#0558be"), '>'
            
        ),
        # rx.image(src=)
        rx.color_mode.button(position=''),
        justify='between',
        width='100%',
        ),
        
        margin_bottom='20px',
        # position='sticky',
        # top='0',
        # # z_index="1000",

    )