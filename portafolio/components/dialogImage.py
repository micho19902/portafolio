import reflex as rx


def dialogImage(image: str) -> rx.Component:
    
    

    return rx.dialog.root(
                    rx.dialog.trigger(
                        rx.image(
                            src=image,
                            height='200px'
                        ),
                    ),
                    rx.dialog.content(
                        rx.dialog.close(
                            rx.icon(
                                tag='x',
                                # size='8',
                                margin_bottom='20px'
                            )
                        ),
                        rx.dialog.description(
                            rx.image(
                                src=image,
                                height='500px',
                                width='auto'
                            ),
                            width='auto'
                        ),                     
                    )
                )