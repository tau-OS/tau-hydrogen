# libhelium is being sunset in October 2026
libhelium is in maintenance mode until Ultramarine's components using it have shifted off (planned for UM45)

libhelium will be deprecated when no more Ultramarine components are using it.

[See our post about the end of the tauOS Project ->](https://blog.fyralabs.com/the-future-of-tauos/)

# Hydrogen

![Light screenshot](logo.png#gh-light-mode-only)
![Dark screenshot](logo-dark.png#gh-dark-mode-only)

![](Hydrogen/scalable/apps/org.gnome.Nautilus.svg)  ![](Hydrogen/scalable/apps/systemsettings.svg)  ![](Hydrogen/scalable/apps/utilities-terminal.svg) ![](Hydrogen/scalable/apps/application-default-icon.svg)

Hydrogen is the default icon theme in tauOS

### Why Hydrogen?

Hydrogen, like the first element in the periodic table, is small yet important.
Our iconset is fairly light and inviting, and simple.

## Vacuuming

It is strongly encouraged to vacuum all vectors with [Inkscape](http://inkscape.org). This keeps the repository lean, clean, and fast for everyone. For convenience, a git pre-commit hook is included. To install, run this command from your local repository folder:

```sh
$ cp pre-commit .git/hooks/
```

## Building

This will install Hydrogen to /usr/share/icons

```sh
$ meson build --prefix=/usr
$ cd build
$ sudo ninja install
```

## Wanted Icons

If you have the time and would like to contribute, the addition of the following icons would be useful:
- [ ] *-filled-symbolic variants of existing symbolics
