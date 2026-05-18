import reflex as rx



def navbar() -> rx.Component:
    return rx.box(
        rx.text(
            '<MICHO/DEVOPS>'
            
        ),
        # rx.image(src=)
        rx.color_mode.button(position='top-right'),

    )