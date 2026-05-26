import reflex as rx
from .dialogImage import dialogImage
from .tecnolog import tecnolog



def body() -> rx.Component:
    return rx.container(
        
            rx.heading(
                'Tenologías...',
                margin_bottom='20px'
            ),
            rx.grid(
                
                tecnolog('docker-svgrepo-com.svg','Docker', '#4351D4'  ),
                tecnolog('oracle-svgrepo-com.svg','Oracle', '#DC9797'  ),
                tecnolog('linux-svgrepo-com.svg','GNU/Linux', '#FCC624'  ),
                tecnolog('python-svgrepo-com.svg','Python', '#249BFC'  ),
                tecnolog('reflex.jpg','Reflex', '#BF00F4'  ),
                tecnolog('github-color-svgrepo-com.svg','GitHUB', '#009BF4'  ),
                tecnolog('postgresql-svgrepo-com.svg','PostgreSQL', '#009BF4'  ),
                tecnolog('ansible-svgrepo-com.svg', 'Ansible', '#FCC624'),
                tecnolog('Zentyal_logo.svg', '', '#009BF4'),
                tecnolog('software-vmware-workstation-svgrepo-com.svg', 'VMWare - ESXi','#FCC624'),
                tecnolog('proxmox-svgrepo-com.svg', 'Proxmox', '#f78400'),
                
                rx.hstack(
                    rx.color_mode_cond(
                        light=rx.image(
                            src='railway_black.png',
                            height='40px',
                            border_radius="20px"
                            
                    ),
                        dark=rx.image(
                            src='railway.png',
                            height='40px',
                            border_radius="20px",

                    )
                ),
                    rx.text(
                        'Railway'
                    ),
                    align='center',
                    border='2px solid',
                    border_radius='30px',
                    padding='1px 10px'

                    
                ),
                

            justify='between',
            # columns='4',
            columns=rx.breakpoints(initial="2", sm="3", lg="4"),
            spacing='2'  

            ),
            rx.heading(
                'Proyectos...',
                margin='60px 0px 20px 0px',
                

            ),
            rx.heading(
                ' - appNotes',
                size='4',
                margin='20px',
                # class_name='tecn_hoover'
            
            ),
            rx.hstack(
                
                rx.text(
                    '''Proyecto de prueba realizado en el camino de aprendizaje de Reflex de Python, 
                    proyecto pensado para llevar un registro de notas almacenadas con fecha, 
                    permite la insercion de nuevas notas, eliminacion y asignacion de un nivel de prioridad en identificadas por color.
                    Este se desplego en produccion en Railway y se lleva control de versiones en GitHUB, las notas son guardadas en una base
                    de datos PostgreSQL, en proceso de implementar una autenticacion(Ya disponible registro de usuarios)''',
                    width='500px',
                    height='auto'
                ),
                
                
                dialogImage('appnotes.png')
                    
            ),
            rx.heading(
                ' - hyprland desktop',
                size='4',
                margin='20px',
            
            ),
            rx.hstack(
                rx.text(
                    '''Proyecto de escritorio basado en Hyprland, con una configuración minimalista y eficiente en GNU/Linux, 
                    orientado a productividad. Ambiente personalizable con atajos de teclado, gestión de ventanas en mosaico, 
                    transparencias sutiles y esquemas de color coherentes. Incluye paneles ligeros, indicadores de sistema, 
                    docks ocultos y una experiencia fluida para desarrollo, navegación y multimedia, manteniendo el sistema rápido y estable.''',
                    width='500px',
                    height='auto'
                ),
                dialogImage('hypr-desktop.png')
            ),
            rx.heading(
                'Certificados',
                margin='60px 0px 20px 0px',
            ),
            
                rx.hstack(
                    rx.heading(
                        '- Linux Essentials LPI',
                        size='4',
                        margin_left='20px',
                        width='200px'
                    ),
                    rx.button(
                        '[PDF]',
                        on_click=rx.download(url='/LE.pdf')
                    ),
                    rx.link(
                        rx.button(
                            'Insignia'
                        ),
                        href='https://www.credly.com/badges/08ba86dc-34fa-437d-a18c-c406a9c0a5a9',
                        is_external=True
                    ),
                    
                    justify='between',
                    align='center',
                    bg="#e3e2e158",
                    color='auto',
                    padding='2px',
                    border_radius='5px',
                    margin_bottom='5px'
                    
                ),
                rx.hstack(
                    rx.heading(
                        '- SQL Interactivo',
                        size='4',
                        margin_left='20px',
                        width='200px'
                    ),
                    rx.button(
                        '[PDF]',
                        on_click=rx.download(url='/assets/29156_05092024.png')
                    ),
                    rx.link(
                        rx.button(
                            'Insignia'
                        ),
                        href='https://tutorialesinteractivos.com/certificados/8f84033e-ac26-4469-ba6f-1242da8d3242',
                        is_external=True
                    ),
                    
                    justify='between',
                    align='center',
                    bg="#e3e2e158",
                    color='auto',
                    padding='2px',
                    border_radius='5px',
                    margin_bottom='5px'
                    
                ),
                rx.hstack(
                    rx.heading(
                        '- Python Interactivo',
                        size='4',
                        margin_left='20px',
                        width='200px'
                    ),
                    rx.button(
                        '[PDF]',
                        on_click=rx.download(url='/34812_15102024.png')
                    ),
                    rx.link(
                        rx.button(
                            'Insignia'
                        ),
                        href='https://tutorialesinteractivos.com/certificados/8f84033e-ac26-4469-ba6f-1242da8d3242',
                        is_external=True
                    ),
                    
                    justify='between',
                    align='center',
                    bg="#e3e2e158",
                    color='auto',
                    padding='2px',
                    border_radius='5px',
                    margin_bottom='5px'
                    
                ),
        
        margin='4px',
        height='auto',
        border_radius='10px',
        # spacing='2px'

        ),