from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import sys

class GridApp(App):
    def build(self):
        # Create a GridLayout with 10 columns
        layout = GridLayout(cols=10)

        # Dictionary to store buttons with IDs 
        cell_dict = {}  
        cell_blacklist = ['cell_0', 'cell_1', 'cell_2', 'cell_3', 'cell_4', 'cell_5', 'cell_6', 'cell_7', 'cell_8', 'cell_9']


    
        # Add buttons to the layout with event handlers
        for i in range(100):
            cell_id = f"cell_{i}"
            button = Button(text="")  # Create button with empty text
            def on_press_handler(instance, cell_id=cell_id):
                print(f"Cell {cell_id} is pressed!")
                if cell_id in cell_dict and cell_id not in cell_blacklist:
                    cell_dict[cell_id].background_color = (0, 2, 204, 1)  # Change background color
            button.bind(on_press=on_press_handler)  # Bind event handler
            # Uncomment these lines to add buttons to dictionary (optional)
            cell_dict[cell_id] = button
            layout.add_widget(button)  # Add button to layout
        for cell_id in cell_blacklist:
            cell_dict[cell_id].background_color = (100, 0, 204, 1)  # Change background color

            


        return layout
if __name__ == "__main__":
    GridApp().run()







    ######## todo
    # 1. add hotbar at top, cells 0-9
    # 2. add placements
    # 3. add saves via yaml file
    # 4. add menu
    # 5.
    # 6.  
    # 7. 
  
