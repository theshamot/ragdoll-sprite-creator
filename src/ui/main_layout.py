import PySimpleGUI as sg

menu_def = [['&File', ['!&Open', '&Save::savekey', '&Save as::saveaskey', '---', '&Settings', 'E&xit']],
            ['&Edit', ['!&Paste', 'Undo'], ],
            ['&Help', '&About'], ]

# left side layout            
left_toolbar = [
    sg.Text("Toolbox"),
    sg.Button("1"),
    sg.Button("2"),
    sg.Button("3"),
]
left_workspace = [
    sg.Graph(   canvas_size=(500,500),
                graph_bottom_left=(-100,-100),
                graph_top_right=(100,100),
                background_color="#fff",
                key="node-canvas",
                enable_events=True,)
]
left_browser = [
    sg.Listbox(values=[], size=(50, 5))
]
left_layout = [
    left_toolbar,
    left_workspace,
    left_browser
]

# right side layout
right_toolbar = [
    sg.Text("Toolbox"),
    sg.Button("1"),
    sg.Button("2"),
    sg.Button("3"),
]
right_workspace = [
    sg.Graph(   canvas_size=(500,500),
                graph_bottom_left=(-100,-100),
                graph_top_right=(100,100),
                background_color="#fff")
]
right_browser = [
    sg.Listbox(values=[], size=(50, 5))
]
right_layout = [
    right_toolbar,
    right_workspace,
    right_browser
]

# create main window
layout = [
    [
        sg.Menu(menu_def, tearoff=False),
        sg.Column(left_layout),
        sg.VSeparator(),
        sg.Column(right_layout),
    ]
]
window = sg.Window(title="Ragdoll sprite creator", layout=layout)

def create_main_window():
    while True:
        event, values = window.read()
        # event, values = window.read(timeout=100) # this will update the window every 100ms

        if event == sg.WIN_CLOSED:
            break

        if event == "node-canvas":
            window["node-canvas"].erase()
            window["node-canvas"].draw_rectangle((0,0), (100,100), fill_color="red")
            window["node-canvas"].draw_text("Hello World", (50,50))
    window.close()

create_main_window()