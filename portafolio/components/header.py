import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src='https://scontent-mia3-2.xx.fbcdn.net/v/t39.30808-6/277170269_2734413586704647_6200820579857454140_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=y9pmdtozLnUQ7kNvwHt5Q74&_nc_oc=Ado3hREYP_aSzypiFHhSYzHEEehgjrTjYxoLGgnXQlRAiw7OT-oh7cxwW32AhEzQYKQ&_nc_zt=23&_nc_ht=scontent-mia3-2.xx&_nc_gid=mMjioq-FhNs9aGvRsPZDRQ&_nc_ss=7b2a8&oh=00_Af4rKClUnPr3EZHosLQ91Rs0d4TjDJ2s6RNSO33T7r-whw&oe=6A17FB94',
                size='9',
                radius='full',
                # border='2px solid red',
                fallback='MG'

            ),
            rx.vstack(
                rx.heading(
                    'Michel Guerrero Obrador',
                            size=rx.breakpoints({'lg':'8', 'md':'5', 'xs':'3'})
                    # size=rx.breakpoints(xl='8',lg='8')
                    
                ),
                rx.tablet_and_desktop(
                rx.code_block(
                    '< DevOps Junior / Devs por Hobby >',
                    language="python",
                    theme=rx.color_mode_cond(
                        light=rx.code_block.themes.one_light,
                        dark=rx.code_block.themes.one_dark,
                    ),
                    
                ),
                ),
                rx.hstack(
                        rx.icon(
                            tag='map-pin-check-inside'

                        ),
                        rx.text(
                            'La Habana, Cuba'
                        )
                    ),
                rx.hstack(
                    rx.link(
                        rx.image(
                            src='github-color-svgrepo-com.svg',
                            height='40px',
                            
                        ),
                        href='https://github.com/micho19902',
                        is_external=True
                    ),
                    rx.link(
                        rx.image(
                            src='reflex.jpg',
                            height='40px',
                            border_radius="20px",
                            
                        ),
                        href='https://reflex.dev/',
                        is_external=True
                    ),
                    rx.link(
                        rx.button(
                            rx.hstack(
                            rx.icon(
                                'mail'
                            ),
                            rx.text(
                                'micho.1990@gmail.com'
                            )
                            ),
                            variant='surface',
                            border_radius='20px',
                            # size='3'
                            size=rx.breakpoints({'lg':'3', 'md':'3', 'xs':'2'}),
                            class_name='mail_to'
                            
                        ),
                        href='mailto:micho.1990@gmail.com',
                        
                    ),
                     rx.link(
                        rx.button(
                            rx.hstack(
                            rx.icon(
                                'mail'
                            ),
                            rx.text(
                                'Solicitar CV'
                            )
                            ),
                            variant='surface',
                            border_radius='20px',
                            # size='3'
                            size=rx.breakpoints({'lg':'3', 'md':'3', 'xs':'2'}),
                            class_name='mail_to',
                            on_click=rx.redirect('/CV Michel Guerrero Obrador.pdf', is_external=True)
                            
                        ),
                        
                    ),
                    spacing='3',
                    align='center'
                ),
                spacing='1',
                padding='5px'
            )
            
        ),
        # border='2px solid white',
        # border_radius='10px',
        margin='4px',
        height=['auto','auto'],
        # bg="#4D4848",
        width=['auto','auto'],
    )