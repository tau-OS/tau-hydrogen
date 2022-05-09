project (
    'co.tauos.Hydrogen',
    version: '0.1.0',
    license : 'GPL3+'
)

i18n = import('i18n')
icon_folder = join_paths(meson.source_root(), 'Hydrogen')
icon_sys_dir = join_paths(get_option('datadir'), 'icons')
icon_dir = join_paths(get_option('datadir'), 'icons', 'Hydrogen')
symlink = join_paths(meson.source_root (), 'meson', 'symlink.py')

# Let's do fancy things
msg_warning = false
msg = '\nPLEASE VERIFY THE CONFIGURATION:'

if (get_option('prefix') == '/usr')
    msg += '\nInstallation prefix:       @0@ ✔'.format (get_option('prefix'))
else
    msg += '\nInstallation prefix:       @0@ ⛔'.format (get_option('prefix'))
    msg_warning = true
endif

if (msg_warning)
    warning(msg + '\n')
else
    message(msg + '\n')
endif

subdir('Hydrogen')

# Let's install
install_subdir(
    icon_folder,
    install_dir : icon_sys_dir
)

install_data(
    join_paths(meson.source_root(), 'logo.png'),
    install_dir: join_paths(icon_dir)
)
