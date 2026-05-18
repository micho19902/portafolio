import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                size='9',
                radius='full',
                border='2px solid red'

            ),
            rx.vstack(
                rx.heading(
                    'Michel Guerrero Obrador'
                ),
                rx.hstack(
                    rx.link(
                        rx.image(
                            src='facebook.svg',
                            height='40px',
                            
                        ),
                    ),
                    rx.link(
                        rx.image(
                            src='github-color-svgrepo-com.svg',
                            height='40px',
                            
                        ),
                    ),
                    rx.link(
                        rx.image(
                            src='reflex.jpg',
                            height='40px',
                            
                        ),
                    ),
                    spacing='6'
                ),
                spacing='7'
            )
            
        ),
        border='2px solid white',
        border_radius='10px',
        margin='4px',
        height='100%',
        # bg="#4D4848",
        width='auto|auto'
    )