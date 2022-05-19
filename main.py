from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    # my_text2 = StringProperty("50")
    text_input_str = StringProperty("Seneca")
    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)


    def on_toggle_button_state(self, widget):

        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
        # print("toggle state: " + widget.state)


    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_slider_value(self, widget):
        # self.my_text2 = str(int(widget.value))
        print("Slider: " + str(int(widget.value)))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text




class StackLayoutExample(StackLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)



#
# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="carvel")
    #     b2 = Button(text="carvel")
    #     b3 = Button(text="carvel")
    #     self.add_widget(b1)
    #     self.add_widget(b3)
    #     self.add_widget(b2)


class MainWidget(Widget):
    pass


class CarvelApp(App):
    def build(self):
        self.icon = 'carvel.ico'
    pass


CarvelApp().run()