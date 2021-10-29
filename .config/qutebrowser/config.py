
### *

## Remove it to not load settings done via the GUI.
config.load_autoconfig(False)

## alias
# c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}


## backend
c.backend = 'webengine'


### key

## key remapping
# c.bindings.key_mappings = {'<Ctrl-[>': '<Escape>', '<Ctrl-6>': '<Ctrl-^>', '<Ctrl-M>': '<Return>', '<Ctrl-J>': '<Return>', '<Shift-Return>': '<Return>', '<Enter>': '<Return>', '<Shift-Enter>': '<Return>', '<Ctrl-Enter>': '<Ctrl-Return>'}


### theme

# from theme import *
config.source('theme.py')


### completion

c.completion.cmd_history_max_items = 100
c.completion.delay = 0
c.completion.height = '50%'
c.completion.min_chars = 1
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history']
c.completion.quick = True

c.completion.scrollbar.padding = 2
c.completion.scrollbar.width = 12

c.completion.show = 'always'
c.completion.shrink = False

# c.completion.timestamp_format = '%Y年 %m月 %d日'
c.completion.timestamp_format = '%Y-%m-%d'

c.completion.use_best_match = False
c.completion.web_history.exclude = []
c.completion.web_history.max_items = -1



### confirm_quit

c.confirm_quit = ['multiple-tabs', 'downloads']


### content

c.content.default_encoding = 'utf-8'
c.content.user_stylesheets = []
c.content.pdfjs = True



### download

c.downloads.location.directory = "$HOME/Downloads"
c.downloads.location.suggestion = 'both'
c.downloads.position = 'bottom'
c.downloads.remove_finished = 2000



### editor

# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.editor.encoding = 'utf-8'



### fonts

# c.fonts.default_family = ["Ricty"]
c.fonts.default_family = []
c.fonts.default_size = "12pt"


### hints

c.hints.border = '1px solid #66cc99'
c.hints.chars = 'asdfghjkl'
c.hints.min_chars = 2
c.hints.mode = 'letter'
c.hints.radius = 3


### message


c.messages.timeout = 2000


### prompt

c.prompt.radius = 0


### scrolling

c.scrolling.bar = 'never'


### statusbar

c.statusbar.widgets = [ 'keypress', 'url', 'history', 'progress', 'tabs']


### tabs

c.tabs.padding = {'top': 2, 'bottom': 2, 'left': 5, 'right': 5}
c.tabs.position = 'top'
# or bottom right top left
c.tabs.show = 'always'
# or always never multiple switching
c.tabs.show_switching_delay = 20000
c.tabs.title.format = '{audio}{index}: {current_title} @ [{scroll_pos}]'
c.tabs.close_mouse_button = "right"

### url

c.url.default_page = 'https://duckduckgo.com'
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'google': 'https://www.google.com/search?q={}'}
c.url.start_pages = 'https://duckduckgo.com'

### zoom

c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '133%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']



### key bindings

# from keybinds import *
config.source('keybinds.py')
