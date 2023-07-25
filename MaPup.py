from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (360, 640)

def initial_graph():
    return {
        'Main Gate (A)': {'Obelisk (B)': 119, 'Tennis Court (Y)': 70, 'Grandstand (E)': 100, 'Oval (F)': 99, 'Community Bldg (G)': 141, 'Interfaith Chapel (H)': 190},
        'Obelisk (B)': {'Main Gate (A)': 118, 'Freedom Park (C)': 28, 'Apolinario Mabini Shrine (D)': 25, 'South Lagoon (T1)': 31, 'PE Bldg (U)': 50, 'Bball & Vball Court (W)': 30, 'Swimming Pool (V)': 53},
        'Freedom Park (C)': {'Obelisk (B)': 28, 'Apolinario Mabini Shrine (D)': 25, 'South Lagoon (T1)': 40, 'North Wing (I)': 26, 'Interfaith Chapel (H)': 76},
        'Apolinario Mabini Shrine (D)': {'Obelisk (B)': 25, 'Freedom Park (C)': 18, 'Interfaith Chapel (H)': 81},
        'Grandstand (E)': {'Main Gate (A)': 100, 'Oval (F)': 41, 'Interfaith Chapel (H)': 83},
        'Oval (F)': {'Main Gate (A)': 99, 'Grandstand (E)': 41, 'Community Bldg (G)': 39, 'Interfaith Chapel (H)': 119},
        'Community Bldg (G)': {'Main Gate (A)': 128, 'Oval (F)': 39, 'Interfaith Chapel (H)': 145},
        'Interfaith Chapel (H)': {'Main Gate (A)': 190, 'Freedom Park (C)': 76, 'Apolinario Mabini Shrine (D)': 81, 'Grandstand (E)': 83, 'Oval (F)': 119, 'Community Bldg (G)': 150, 'North Wing (I)': 53, 'Main Building (L)': 53, 'East Wing (J)': 65},
        'North Wing (I)': {'Freedom Park (C)': 26, 'Interfaith Chapel (H)': 53, 'Main Building (L)': 42, 'Amphitheater (S)': 56},
        'East Wing (J)': {'Interfaith Chapel (H)': 65, 'Main Building (L)': 50, 'South Wing (K)': 38},
        'South Wing (K)': {'East Wing (J)': 38, 'Main Building (L)': 32, 'West Building (M)': 37},
        'Main Building (L)': {'North Wing (I)': 42, 'Interfaith Chapel (H)': 59, 'East Wing (J)': 50, 'South Wing (K)': 32, 'West Building (M)': 44, 'Amphitheater (S)': 32},
        'West Building (M)': {'Amphitheater (S)': 43, 'Main Building (L)': 44, 'South Wing (K)': 37, 'Student Canteen (N)': 23},
        'Student Canteen (N)': {'West Building (M)': 23, 'Amphitheater (S)': 62, 'North Lagoon (T2)': 67, 'Charlie Del Rosario Bldg (O)': 29},
        'Charlie Del Rosario Bldg (O)': {'North Lagoon (T2)': 31, 'Ninoy Aquino Library (R)': 64, 'Student Canteen (N)': 29},
        'Printing Press Bldg (P)': {'Laboratory High School (Q)': 125},
        'Laboratory High School (Q)': {'Printing Press Bldg (P)': 125, 'Ninoy Aquino Library (R)': 64},
        'Ninoy Aquino Library (R)': {'Charlie Del Rosario Bldg (O)': 64, 'North Lagoon (T2)': 51, 'PE Bldg (U)': 96,  'Laboratory High School (Q)': 64},
        'Amphitheater (S)': {'South Lagoon (T1)': 41, 'Student Canteen (N)': 62, 'West Building (M)': 43, 'Main Building (L)': 32, 'North Wing (I)': 56, 'North Lagoon (T2)': 30},
        'South Lagoon (T1)': {'Obelisk (B)': 31, 'Freedom Park (C)': 40, 'Amphitheater (S)': 41, 'North Lagoon (T2)': 130},
        'North Lagoon (T2)': {'South Lagoon (T1)': 130, 'Amphitheater (S)': 30, 'Charlie Del Rosario Bldg (O)': 31, 'Ninoy Aquino Library (R)': 51, 'Student Canteen (N)': 67},
        'PE Bldg (U)': {'Ninoy Aquino Library (R)': 96, 'Obelisk (B)': 50, 'Swimming Pool (V)': 45},
        'Swimming Pool (V)': {'PE Bldg (U)': 45, 'Bball & Vball Court (W)': 44, 'Gymnasium (X)': 71, 'Obelisk (B)': 53},
        'Bball & Vball Court (W)': {'Obelisk (B)': 30, 'Tennis Court (Y)': 47, 'Swimming Pool (V)': 44},
        'Gymnasium (X)': {'Swimming Pool (V)': 71, 'Tennis Court (Y)': 27, 'Research Center (Z)': 25},
        'Tennis Court (Y)': {'Main Gate (A)': 70, 'Bball & Vball Court (W)': 47, 'Gymnasium (X)': 25, 'Research Center (Z)': 42},
        'Research Center (Z)': {'Tennis Court (Y)': 42, 'Gymnasium (X)': 25}
    }

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.source_buttons = []
        self.destination_buttons = []
        self.source = None
        self.destination = None
        self.graph = initial_graph()
        self.create_buttons()
        self.icon = "Image/icon.png"

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.create_buttons()

    def create_buttons(self):
        pass

class SourceMap(Screen):
    def __init__(self, **kwargs):
        super(SourceMap, self).__init__(**kwargs)
        self.create_buttons()

    def create_buttons(self):
        pass

class SourceScreen(Screen):
    def __init__(self, **kwargs):
        super(SourceScreen, self).__init__(**kwargs)
        self.building_image = ''
        self.create_buttons()

    def create_buttons(self):
        source_grid = self.ids.source_grid

        for node in initial_graph():
            button = Button(
                text=node,
                size_hint=(None, None),
                size=(200, 80),
                background_color=(181 / 255, 19 / 255, 0 / 255, 0.85),
            )
            button.bind(on_release=self.select_source)
            source_grid.add_widget(button)

    @staticmethod
    def select_source(button):
        app = App.get_running_app()
        app.source = button.text
        app.sourcemap = "Assets/" + button.text + ".png"
        print(f"Selected source: {app.source}")

        app.root.current = 'source_image_screen'

class SourceImageScreen(Screen):
    def __init__(self, **kwargs):
        super(SourceImageScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        app = App.get_running_app()
        source_image = app.sourcemap
        if source_image:
            image_widget = self.ids.source_image
            image_widget.source = source_image

class SelectedImage(Screen):
    def __init__(self, **kwargs):
        super(SelectedImage, self).__init__(**kwargs)

    def on_enter(self, *args):
        app = App.get_running_app()
        destination_image = app.destinationmap
        if destination_image:
            image_widget = self.ids.destination_image
            image_widget.source = destination_image

class DestinationMap(Screen):
    def __init__(self, **kwargs):
        super(DestinationMap, self).__init__(**kwargs)
        self.create_buttons()

    def create_buttons(self):
        pass

class DestinationScreen(Screen):
    def __init__(self, **kwargs):
        super(DestinationScreen, self).__init__(**kwargs)
        self.create_buttons()

    def create_buttons(self):
        destination_grid = self.ids.destination_grid

        for node in initial_graph():
            button = Button(
                text=node,
                size_hint=(None, None),
                size=(200, 80),
                background_color=(181 / 255, 19 / 255, 0 / 255, 0.85),
            )
            button.bind(on_release=self.select_destination)
            destination_grid.add_widget(button)

    @staticmethod
    def select_destination(button):
        app = App.get_running_app()
        app.destination = button.text
        print(f"Selected destination: {app.destination}")

class PathScreen(Screen):
    def find_shortest_path(self):
        app = App.get_running_app()
        if app.source and app.destination:
            path, total_distance = app.calculate_shortest_path(app.source, app.destination)
            if path:
                result_label = self.ids.result_label
                result_label.text = ' -> '.join(path)
                meters_label = self.ids.meters_label
                meters_label.text = f"Total Distance: {total_distance} meters"
        else:
            print("Please select a source and destination.")

class ViewMapScreen(Screen):
    def __init__(self, **kwargs):
        super(ViewMapScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        app = App.get_running_app()
        destination_image = app.destination
        if destination_image:
            image_widget = self.ids.destination_image
            image_widget.source = destination_image

class MaPup(App):
    def __init__(self):
        super().__init__()
        self.graph = initial_graph()
        self.destinationmap = None
        self.destination = None
        self.source = None
        self.sourcemap = None
        self.start = None

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(SourceMap(name='sourcemap'))
        sm.add_widget(SourceScreen(name='source'))
        sm.add_widget(DestinationMap(name='destinationmap'))
        sm.add_widget(DestinationScreen(name='destination'))
        sm.add_widget(PathScreen(name='path'))
        sm.add_widget(SourceImageScreen(name='source_image_screen'))
        sm.add_widget(SelectedImage(name='selected_image'))
        self.icon = "Image/icon.png"
        return sm

    def calculate_shortest_path(self, source, destination):
        path = {}
        meters = {}
        adj_node = {}
        queue = []

        for node in self.graph:
            path[node] = float("inf")
            meters[node] = float("inf")
            adj_node[node] = None
            queue.append(node)

        path[source] = 0
        meters[source] = 0

        while queue:
            key_min = queue[0]
            min_val = path[key_min]
            for n in range(1, len(queue)):
                if path[queue[n]] < min_val:
                    key_min = queue[n]
                    min_val = path[key_min]
            cur = key_min
            queue.remove(cur)

            for i in self.graph[cur]:
                alternate = self.graph[cur][i] + path[cur]
                if path[i] > alternate:
                    path[i] = alternate
                    meters[i] = meters[cur] + self.graph[cur][i]
                    adj_node[i] = cur

        path_nodes = [destination]
        while True:
            destination = adj_node[destination]
            if destination is None:
                break
            path_nodes.append(destination)

        path_nodes.reverse()
        return path_nodes, meters[self.destination]

kv = Builder.load_file('MaPup.kv')

if __name__ == '__main__':
    MaPup().run()
