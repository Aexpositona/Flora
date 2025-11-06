import tkinter as tk

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, **kwargs):
        width = kwargs.pop('width', 300)
        height = kwargs.pop('height', 60)
        bg_color = kwargs.pop('bg', '#a8ad8d')
        fg_color = kwargs.pop('fg', 'white')
        font = kwargs.pop('font', ("Roboto", 20, "bold"))
        parent_bg = kwargs.pop('parent_bg', '#FDF6E3')

        tk.Canvas.__init__(self, parent, width=width, height=height,
                          bg=parent_bg,
                          highlightthickness=0, **kwargs)

        self.command = command
        self.bg_color = bg_color
        self.hover_color = '#999e7e'
        self.fg_color = fg_color

        self.rect = self.create_rounded_rectangle(2, 2, width-2, height-2, radius=8, fill=bg_color, outline="")

        # Texto centrado (icono y texto juntos)
        self.text = self.create_text(width/2, height/2, text=text, fill=fg_color, font=font)
        self.icon = None

        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=16, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_click(self, event):
        if self.command:
            self.command()

    def _on_enter(self, event):
        self.itemconfig(self.rect, fill=self.hover_color)

    def _on_leave(self, event):
        self.itemconfig(self.rect, fill=self.bg_color)
