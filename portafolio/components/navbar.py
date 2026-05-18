import reflex as rx



def navbar() -> rx.Component:
    return rx.box(
        rx.text(
            'navbar'
            
        ),
        rx.color_mode.button(position='top-right'),

    )