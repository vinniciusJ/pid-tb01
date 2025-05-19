def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.setParent(None)
        else:
            sub_layout = item.layout()
            if sub_layout:
                clear_layout(sub_layout)
