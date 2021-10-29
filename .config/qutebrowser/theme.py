

### theme



# config = ConfigAPI  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
# c = ConfigContainer  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103
# c = ConfigContainer.val

# from qutebrowser.config import config

# c = config.val

config = config
c = c



### colors

back_gray = '#666666'
back_black = '#000000'
back_black_sub = '#333333'
back_green = '#336633'
back_blue = '#0066cc'

border_green = '#33cc33'
border_blue = '#3333cc'

text_white = '#ffffff'
text_red = '#ff6666'
text_green = "#33ff66"

## completion

c.colors.completion.category.bg = back_gray
c.colors.completion.category.border.bottom = border_blue
c.colors.completion.category.border.top = border_blue
c.colors.completion.category.fg = text_white

c.colors.completion.fg = ['white', text_red, 'white']

c.colors.completion.item.selected.bg = back_blue
c.colors.completion.item.selected.border.bottom = '#bbbb00'
c.colors.completion.item.selected.border.top = '#bbbb00'
c.colors.completion.item.selected.fg = text_white
c.colors.completion.item.selected.match.fg = text_green
c.colors.completion.match.fg = text_green

c.colors.completion.odd.bg = back_black
c.colors.completion.even.bg = back_black

c.colors.completion.scrollbar.bg = back_blue
c.colors.completion.scrollbar.fg = back_gray


## context menu

c.colors.contextmenu.menu.bg = back_black_sub
c.colors.contextmenu.menu.fg = text_white
c.colors.contextmenu.selected.bg = back_blue
c.colors.contextmenu.selected.fg = text_green


## downloads

c.colors.downloads.bar.bg = back_gray
c.colors.downloads.error.bg = 'red'
c.colors.downloads.error.fg = 'white'
c.colors.downloads.start.bg = '#0000aa'
c.colors.downloads.start.fg = 'white'
c.colors.downloads.stop.bg = '#00aa00'
c.colors.downloads.stop.fg = 'white'

c.colors.downloads.system.bg = 'rgb'
c.colors.downloads.system.fg = 'rgb'


## hints

c.colors.hints.bg = 'rgba(0.7, 0.8, 1.0, 0.7)'
c.colors.hints.fg = text_white
c.colors.hints.match.fg = text_green

c.colors.keyhint.bg = 'rgba(0.7, 1.0, 0.8, 0.7)'
c.colors.keyhint.fg = text_white
c.colors.keyhint.suffix.fg = text_green

## messages

c.colors.messages.error.bg = 'red'
c.colors.messages.error.border = '#bb0000'
c.colors.messages.error.fg = 'white'

c.colors.messages.info.bg = 'black'
c.colors.messages.info.border = '#333333'
c.colors.messages.info.fg = 'white'

c.colors.messages.warning.bg = 'darkorange'
c.colors.messages.warning.border = '#d47300'
c.colors.messages.warning.fg = 'white'

## prompt

c.colors.prompts.bg = '#444444'
c.colors.prompts.border = '1px solid gray'
c.colors.prompts.fg = 'white'
c.colors.prompts.selected.bg = 'grey'

## statusbar

c.colors.statusbar.caret.bg = 'purple'
c.colors.statusbar.caret.fg = 'white'
c.colors.statusbar.caret.selection.bg = '#a12dff'
c.colors.statusbar.caret.selection.fg = 'white'

c.colors.statusbar.command.bg = 'black'
c.colors.statusbar.command.fg = 'white'
c.colors.statusbar.command.private.bg = 'darkslategray'
c.colors.statusbar.command.private.fg = 'white'

c.colors.statusbar.insert.bg = 'darkgreen'
c.colors.statusbar.insert.fg = 'white'

c.colors.statusbar.normal.bg = 'black'
c.colors.statusbar.normal.fg = 'white'

c.colors.statusbar.passthrough.bg = 'darkblue'
c.colors.statusbar.passthrough.fg = 'white'

c.colors.statusbar.private.bg = '#666666'
c.colors.statusbar.private.fg = 'white'

c.colors.statusbar.progress.bg = 'white'

c.colors.statusbar.url.error.fg = 'orange'
c.colors.statusbar.url.fg = 'white'
c.colors.statusbar.url.hover.fg = 'aqua'
c.colors.statusbar.url.success.http.fg = 'white'
c.colors.statusbar.url.success.https.fg = 'lime'
c.colors.statusbar.url.warn.fg = 'yellow'


## tabs


c.colors.tabs.bar.bg = '#555555'

c.colors.tabs.even.bg = 'darkgrey'
c.colors.tabs.even.fg = 'white'

c.colors.tabs.indicator.error = '#ff0000'
c.colors.tabs.indicator.start = '#0000aa'
c.colors.tabs.indicator.stop = '#00aa00'

c.colors.tabs.indicator.system = 'rgb'

c.colors.tabs.odd.bg = 'grey'
c.colors.tabs.odd.fg = 'white'

c.colors.tabs.pinned.even.bg = 'darkseagreen'
c.colors.tabs.pinned.even.fg = 'white'

c.colors.tabs.pinned.odd.bg = 'seagreen'
c.colors.tabs.pinned.odd.fg = 'white'

c.colors.tabs.pinned.selected.even.bg = 'black'
c.colors.tabs.pinned.selected.even.fg = 'white'

c.colors.tabs.pinned.selected.odd.bg = 'black'
c.colors.tabs.pinned.selected.odd.fg = 'white'

c.colors.tabs.selected.even.bg = 'black'
c.colors.tabs.selected.even.fg = 'white'

c.colors.tabs.selected.odd.bg = 'black'
c.colors.tabs.selected.odd.fg = 'white'


## webpage

c.colors.webpage.bg = 'white'


## dark

# c.colors.webpage.prefers_color_scheme_dark = True

