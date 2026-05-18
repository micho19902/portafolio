import reflex as rx




def footer() -> rx.Component:

    return rx.container(
        rx.heading(
            'Footer'
        ),
        border='2px solid white',
        margin='4px',
        height='100px',
        border_radius='10px',
    )