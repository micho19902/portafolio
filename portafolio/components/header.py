import reflex as rx


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.avatar(
                src='https://scontent-mia3-2.xx.fbcdn.net/v/t39.30808-1/277170269_2734413586704647_6200820579857454140_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=107&ccb=1-7&_nc_sid=e99d92&_nc_ohc=iqaNc98OSqUQ7kNvwFOXS5c&_nc_oc=AdoxrO9P2r0MIcrfWyfwkzmi8Npf6JGde-535wMA_kXL9wS8PhkhtHXClC7nmmt3Cks&_nc_zt=24&_nc_ht=scontent-mia3-2.xx&_nc_gid=HFWjEEH38K1AF0ulbJcWdQ&_nc_ss=7b2a8&oh=00_Af5GSaTuf8PF-yAU9P_ugsLjJv3At5ZCID0d0_MhGufWmQ&oe=6A11A792',
                size='9',
                radius='full',
                # border='2px solid red',
                fallback='MG'

            ),
            rx.vstack(
                rx.heading(
                    'Michel Guerrero Obrador',
                    size='8'
                    
                ),
                rx.code_block(
                    '< DevOps Junior / Devs por Hobby >',
                    language="python",
                    theme=rx.color_mode_cond(
                        light=rx.code_block.themes.one_light,
                        dark=rx.code_block.themes.one_dark,
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
                    
                    # rx.link(
                    #     rx.image(
                    #         src='facebook.svg',
                    #         height='40px',
                            
                    #     ),
                    #     href=
                    # ),
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
                            size='3'
                        ),
                        href='mailto:micho.1990@gmail.com'
                    ),
                    spacing='3'
                ),
                spacing='1',
                padding='5px'
            )
            
        ),
        # border='2px solid white',
        # border_radius='10px',
        margin='4px',
        height='auto|auto',
        # bg="#4D4848",
        width='auto|auto'
    )