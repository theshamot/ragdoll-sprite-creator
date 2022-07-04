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
    sg.Canvas(size=(500,500), background_color="#fff")
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
    sg.Canvas(size=(500,500), background_color="#fff")
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

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()