import reflex as rx


def dialogImage(image: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.image(
                src=image,
                width=rx.breakpoints(xs='300px', md='330px', xl='360px'),
                # max_width=rx.breakpoints(xs='300px', md='250px', xl='360px'),
                # height='150px',
                height=rx.breakpoints(xs='150px', md='200px', xl='200px'),
                border_radius='20px',
                class_name='mask_image'
    #             style={
    #     "mask_image": "radial-gradient(circle, black 60%, transparent 90%)",
    # }
                
                
            )
        ),
        rx.dialog.content(
            rx.dialog.close(
                rx.icon(tag='x', margin_bottom='20px')
            ),
            rx.dialog.description(
                rx.image(src=image, width='100%', max_width='100vw', height='auto'),
                width='auto',
                
            )
        )
    )
