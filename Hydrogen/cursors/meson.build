cursor_dir = join_paths(icon_dir, 'Hydrogen', 'cursors')
rsvg = find_program('rsvg-convert')
xcursorgen = find_program('xcursorgen')

cursors = [
    'all-scroll',
    'bottom_tee',
    'copy',
    'cross',
    'crosshair',
    'dnd-none',
    'dotbox',
    'hand1',
    'left_ptr',
    'left_tee',
    'link',
    'll_angle',
    'lr_angle',
    'move',
    'no-drop',
    'not-allowed',
    'pencil',
    'plus',
    'pointer',
    'right_ptr',
    'right_tee',
    'sb_down_arrow',
    'sb_h_double_arrow',
    'sb_left_arrow',
    'sb_right_arrow',
    'sb_up_arrow',
    'sb_v_double_arrow',
    'tcross',
    'text',
    'top_tee',
    'ul_angle',
    'ur_angle',
    'vertical-text',
    'X_cursor',
    'zoom-in',
    'zoom-out'
]

sizes = [
    '24',
    '32',
    '48',
    '64',
    '96'
]

foreach size: sizes
    run_command('mkdir', join_paths (meson.build_root(), 'cursors', size + 'x' + size))

    foreach cursor : cursors
            message('rendering: ' + size + 'x' + size + '/' + cursor + '.png')

            run_command(
                rsvg, '--format', 'png',
                '--width=@0@'.format(size), '--height=@0@'.format(size),
                '--output', '@0@.png'.format(join_paths (meson.build_root(), 'cursors', size + 'x' + size, cursor)),
                join_paths ('24', cursor + '.svg')
            )
    endforeach
endforeach

cursors += [
    'left_ptr_watch',
    'watch'
]

foreach cursor : cursors
    message('generating: ' + cursor)

    run_command(
        xcursorgen,
        cursor + '.in',
        '-p', join_paths (meson.build_root(), 'cursors'),
        join_paths (meson.build_root(), 'cursors', cursor)
    )

    install_data(
        join_paths (meson.build_root(), 'cursors', cursor),
        install_dir: cursor_dir
    )
endforeach

links = []

links += [[
  'copy',
  [
      '6407b0e94181790501fd1e167b474872',
      '1081e37283d90000800003c07f3ef6bf'
  ]
]]

links += [[
  'cross',
  [
      'diamond_cross',
      'cross_reverse'
  ]
]]

links += [[
    'dnd-none',
    [
        'grabbing'
    ]
]]

links += [[
  'dotbox',
  [
      'target',
      'icon',
      'draped_box',
      'dot_box_mask'
  ]
]]

links += [[
  'hand1',
  [
      'grab',
      'fleur'
  ]
]]

links += [[
  'left_ptr',
  [
      'arrow',
      'top_left_arrow',
      '08e8e1c95fe2fc01f976f1e063a24ccd',
      '3ecb610c1bf2410f44200f48c40d3599'
  ]
]]

links += [[
  'link',
  [
      '3085a0e285430894940527032f8b26df',
      '640fb0e74195791501fd1ed57b41487f'
  ]
]]

links += [[
  'move',
  [
      '9081237383d90e509aa00f00170e968f',
      '4498f0e0c1937ffe01fd06f973665830'
  ]
]]

links += [[
  'not-allowed',
  [
      'crossed_circle',
      '03b6e0fcb3499374a867c041f52298f0'
  ]
]]

links += [[
  'pointer',
  [
      'hand',
      'hand2',
      '9d800788f1b08800ae810202380a0822'
  ]
]]

links += [[
  'plus',
  [
      'cell'
  ]
]]


links += [[
  'right_ptr',
  [
      'draft_small',
      'draft_large'
  ]
]]

links += [[
  'sb_h_double_arrow',
  [
      'h_double_arrow',
      'left_side',
      'right_side',
      '028006030e0e7ebffc7f7070c0600140',
      '14fef782d02440884392942c11205230'
  ]
]]

links += [[
  'sb_v_double_arrow',
  [
      'bottom_side',
      'double_arrow',
      'top_side',
      'v_double_arrow',
      '00008160000006810000408080010102',
      '2870a09082c103050810ffdffffe0204'
  ]
]]

links += [[
  'text',
  [
      'xterm'
  ]
]]

links += [[
  'X_cursor',
  [
      'pirate'
  ]
]]

foreach link_entry : links
    src = link_entry[0]
    foreach dest : link_entry[1]
        meson.add_install_script(
            symlink,
            '--src', join_paths (cursor_dir, src),
            '--dest', join_paths (cursor_dir, dest)
        )
    endforeach
endforeach

install_data(
    'cursor.theme',
    install_dir: icon_dir
)
