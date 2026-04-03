import flet as ft
import requests
from Core_front.settings import KEY_JSON,URL_BASE,URL_WAY_START_MENU
from Validation.Page_start_meny import ValidationStartMenu
from pydantic import ValidationError
from Core_front.config_log import get_logger

logger = get_logger(__name__) 

class Start_menu():
    def __init__(self):
        self.product_input = ft.TextField(label='Write the Product',hint_text='example : Meat')
        self.quantity_input = ft.TextField(label='Quantity',hint_text='number: 10, 20, 100')
        self.category_dropdown = ft.Dropdown(
            label="Select Category",
            options=[ft.dropdown.Option("kg"),
            ft.dropdown.Option("gramm")]
        )
        self.logger = logger
        self.progress_ring = ft.ProgressRing(color=ft.Colors.GREEN,visible=False)
        self.controls_error = ft.Text('The Fields its not complete',color=ft.Colors.RED)
        self.api_response =ft.Column([])
        self.success = False

        self.animation = ft.Animation(
            duration=500,
            curve=ft.AnimationCurve.EASE_IN_OUT
        )

        self.container_api_response = ft.Container(content=self.api_response,height=50)
        self.container_api_response.animate = self.animation
        self.container_api_response.opacity = 0
        self.container_api_response.offset = ft.Offset(0,0.5)
        
        self.container_controls_error = ft.Container(content=self.controls_error,height=50)
        self.container_controls_error.animate = self.animation
        self.container_controls_error.opacity = 0
        self.container_controls_error.offset = ft.Offset(0,0.5)

    def get_and_save_success(self):
        self.success = True

        if self.status == requests.codes.ok:
            self.logger.debug('the class Start_menu method get_and_save_success started with status Ok')
            items = self.json['items']
            self.api_response.controls.clear()

            for key in KEY_JSON:
                logger.debug(f'class Start_meny method get_and_save_success get {items[key]}\n')
                self.api_response.controls.append(ft.Text(f'{key.capitalize()}: {items[key]}',height=30))

        else:
            message = self.json.get('message',None)
            self.logger.debug(f'the class Start_menu method get_and_save_success with {message}')

            if message:
                self.logger.debug('the class Start_menu method get_and_save_success started with message error from Api')
                self.api_response.controls.append(ft.Text(f'{message}',color=ft.Colors.RED))
                self.logger.debug(f'class Start_meny method render get_message')

            else:
                self.logger.debug('the class Start_menu method get_and_save_success started with status 422 from Api')
                self.api_response.controls.append(ft.Text(f'The Fields is incorrect',color=ft.Colors.RED))

    def reset_containers(self):
        self.api_response.controls.clear()
        self.container_api_response.opacity = 0
        self.container_api_response.offset = ft.Offset(0,0.5)
        
        self.container_controls_error.opacity = 0
        self.container_controls_error.offset = ft.Offset(0,0.5)

    def start_animation(self):
        
        if self.success == True:
            self.logger.debug(f'the class Start_menu method start_animation started with True')
            container = self.container_api_response
        elif self.success == False:
            self.logger.debug(f'the class Start_menu method start_animation started with False')
            container = self.container_controls_error

        container.opacity = 1
        container.offset = ft.Offset(0,0)
            
    def save_atributs(self,event, status :int, json : dict):
        self.logger.debug(f'the class Start_menu method save_atributs started status: {status},\n json: {json}')
        self.event = event
        self.status = status
        self.json = json

    def dispatch(self,event=None,status=None,json=None):
        self.logger.debug('the class Start_menu method dispatch is started')

        if status:
            self.logger.debug('the class Start_menu method dispatch status is not None')
            self.save_atributs(event,status,json)
            self.get_and_save_success()
            self.start_animation()

        else:
            self.logger.debug('the class Start_menu method dispatch status is None')
            self.start_animation()

    def send_request(self,event):
        
        self.reset_containers()

        self.logger.debug('class Start_menu method send_request')

        try:
            ValidationStartMenu(
                product=self.product_input.value,
                mass=self.category_dropdown.value,
                number=self.quantity_input.value
            )
            self.logger.debug('class Start_menu method send_request validate fields')

        except ValidationError:
            self.logger.debug('class Start_menu method send_request get ValidationError start dispatch method')
            self.dispatch()
            return
        
        response = requests.post(
                            f'{URL_BASE}{URL_WAY_START_MENU}', 
                            json={"product":self.product_input.value,
                                    "mass":self.category_dropdown.value,
                                    "number":self.quantity_input.value}
        )
        self.logger.debug('class Start_menu method send_request send API request')

        self.dispatch(event,status=response.status_code,json=response.json())


    def get_start_menu(self):
        
        return ft.Column([

            ft.Text('Hello this is Nutrient-Calculator',
                    size=20,
                    height=40,
                    color=ft.Colors.GREEN
            ),

            ft.Divider(
                height=20,
                color=ft.Colors.TRANSPARENT
            ),

            ft.Row([
                self.product_input,
                self.quantity_input,
                self.category_dropdown
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            
            ft.Divider(
                height=20,
                       color=ft.Colors.TRANSPARENT
            ),

            ft.Button(
                "   Calculate   ",
                color=ft.Colors.GREEN,
                on_click=self.send_request,
                width=200,
                height=40
            ),

            self.progress_ring,

            ft.Divider(height=10,
                color=ft.Colors.TRANSPARENT
            ),

            self.container_controls_error,
            self.container_api_response
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )


start_menu =Start_menu()
