# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#color import
from colors import colors

# mod keys
mod = "mod4"

# processes/apps file path
terminal = guess_terminal()
apath = "/usr/bin/"
snap = "/snap/bin/"
# wallpaper path
wallp = "~/Downloads/animecity.jpg"

#custom funtion
def open_pavu():
    qtile.cmd_spawn("pavucontrol")

def longNameParse(text): 
    apps=["Chromium", "Firefox", "Google Chrome"]
    for string in apps: #Add any other apps that have long names here
        if string in text:
            text = string
        else:
            text = text
    return text

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
        ),
    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"
        ),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
        ),
    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"
        ),
    Key([mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
        ),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
        ),
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
        ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", 
    	lazy.layout.grow_left(), 
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "l", 
    	lazy.layout.grow_right(), 
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "j", 
    	lazy.layout.grow_down(), 
        desc="Grow window down"
        ),
    Key([mod, "control"], "k", 
    	lazy.layout.grow_up(), 
        desc="Grow window up"
        ),
    Key([mod], "n", 
    	lazy.layout.normalize(), 
        desc="Reset all window sizes"
        ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Launch process/apps
    Key([mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
        ),
    Key([mod], "b", 
        lazy.spawn("google-chrome"), 
        desc="Launch FireFox"
        ),
    Key([mod], "f", 
        lazy.spawn("thunar"), 
        desc="Launch File Manager"
        ),
    Key([mod], "v", 
        lazy.spawn("vlc"), 
        desc="Launch VLC Media"
        ),
    Key([mod], "c", 
        lazy.spawn("code"), 
        desc="Launch VScode"
        ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
        ),
    Key([mod], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
        ),
    Key([mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
        ),
    Key([mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
        ),
    Key([mod], "r", 
        lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"
        ),
    # my custom windos setting
    Key([mod], "x", 
        lazy.window.disable_floating(), 
        desc="Disable floating window"
        ),
    Key([mod, "control"], "x", 
        lazy.window.enable_floating(), 
        desc="Enable floating window"
        ),
    Key([mod, "control"], "m", 
        lazy.window.toggle_maximize(), 
        desc="Maximize window"
        ),
    Key([mod], "m", 
        lazy.window.toggle_minimize(), 
        desc="Minimize window"
        ),
]


# # Defult group setup start --
# groups = [Group(i) for i in "123456789"]
# groups = [Group(i) for i in ("DEV", "WWW", "SYS", "DOC", "VBOX", "CHAT","MUS", "VID",)]
groups=[
    Group("1", layout="bsp", label="󰎤"),
    Group("2", layout="bsp", label="󰎧"),
    Group("3", layout="bsp", label="󰎪"),
    Group("4", layout="bsp", label="󰎭"),
    Group("5", layout="bsp", label="󰎱"),
    Group("6", layout="bsp", label="󰎳"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
# # Defult group setup end --

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(border_focus='#917FB3', border_on_single=True, border_width=3, margin=6, margin_on_single=5),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="sans",
    # font="QDBetterComicSans",
    font="MesloLGL Nerd Font Mono",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# widget.TextBox(
#                 text="",
#                 background = colors[6],
#                 foreground = '#000000',
#                 padding=0,
#                 fontsize = 32
#                 ),


screens = [
    Screen(
    	wallpaper = "/home/minhaz/Downloads/Pictures/violetPlanet.jpg",
    	wallpaper_mode = 'fill',
        top=bar.Bar(
            [
                widget.Spacer(
                    length=5
                ),
                widget.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths= [os.path.expanduser("~/.config/qtile/icons/")],
                ),
                widget.CurrentLayout(
                    foreground=colors[15], 
                ),
                widget.Spacer(
                    length=5
                ),
                widget.GroupBox(
                	highlight_method='line',
                    highlight_color = colors[1],
                    block_highlight_text_color=colors[15],
                    active= colors[16],
                    inactive= colors[17],
                	invert_mouse_wheel=False,
                    fontsize=20,
                    padding=5,

                ),
                widget.Spacer(
                    length=10
                ),
                widget.Prompt(),
                widget.WindowName(
                    parse_text=longNameParse,
                    foreground=colors[0],
                    mouse_callbacks={"Button1": lazy.window.toggle_minimize()},
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Spacer(
                    length=8
                ),
                # Notify wigdet
                widget.Notify(),
                # DiskFree widget
                widget.Sep(
                    foreground = colors[7],
                    linewidth=2,
                ),
                widget.TextBox(
                    text=" ", #wifi icon
                    foreground = colors[7],
                    fontsize = 20
                ),
                widget.DF(
                    visible_on_warn=False,
                    foreground = colors[7],
                ),
                # Net widget
                widget.Sep(
                    foreground = colors[5],
                    linewidth=2,
                ),
                widget.TextBox(
                    text=" ", #wifi icon
                    foreground = colors[5],
                    fontsize = 22
                ),
                widget.Net(
                    foreground = colors[5],
                    format='{down}↓↑{up}'
                ),
                # PulseVolume widget
                widget.Sep(
                    foreground = colors[4],
                    linewidth=2,
                ),
                widget.TextBox(
                    text=" 󰕾", #volume icon
                    foreground = colors[4],
                    fontsize = 15
                ),
                widget.PulseVolume(
                    limit_max_volume="True",
                    update_interval=0.1,
                    mouse_callbacks={"Button1": open_pavu},
                    foreground = colors[4],
                ),
                # Clock widget
                widget.Sep(
                    foreground = colors[3],
                    linewidth=2,
                ),
                widget.TextBox(
                    text=" 󰥔", #clock icon
                    foreground = colors[3],
                    padding=8,
                    fontsize = 15
                ),
                widget.Clock(
                    format="%-I:%M %p",
                    foreground = colors[3],
                ),
                widget.Spacer(
                    length=10
                ),
            ],
            28,
            background = colors[1]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
