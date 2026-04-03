import flet as ft
import requests
from Core_front.settings import KEY_JSON
from Controls.Page_start_menu import start_menu
from Core_front.config_log import get_logger

logger = get_logger(__name__) 

def main(page:ft.Page):
    #Base
    page.title = 'Nutrient-Calculator'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    #Logic
    def change_theme(event):
        if event.page.theme_mode == ft.ThemeMode.LIGHT:
            logger.debug('func change_theme in func main theme = DARK')
            event.page.theme_mode = ft.ThemeMode.DARK
        else:
            logger.debug('func change_theme in func main theme = LIGHT')
            event.page.theme_mode = ft.ThemeMode.LIGHT
    
    #Variable
    change_theme = ft.Row([
        ft.Button(
            'Change Theme',
            color=ft.Colors.GREEN,
            on_click=change_theme,)
    ],
        alignment=ft.MainAxisAlignment.END,
    )

    container_change_theme = ft.Container(
        content=change_theme,
        alignment=ft.alignment.Alignment.TOP_RIGHT,
        width=page.width,
    )
    
    container_start_menu = ft.Container(
        content=start_menu.get_start_menu(),
        alignment=ft.alignment.Alignment.CENTER,
    )
    

    #add Page
    page.add(
            container_change_theme,
            ft.Divider(height=50,color=ft.Colors.TRANSPARENT),
            container_start_menu,
            
    )

ft.app(target=main)