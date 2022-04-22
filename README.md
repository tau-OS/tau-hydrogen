# Hydrogen

![Light screenshot](logo.png#gh-light-mode-only)
![Dark screenshot](logo-dark.png#gh-dark-mode-only)

![](Hydrogen/scalable/apps/org.gnome.Nautilus.svg)  ![](Hydrogen/scalable/apps/systemsettings.svg)  ![](Hydrogen/scalable/apps/org.gnome.Weather.svg)

Hydrogen is the default icon theme in tauOS

### Why Hydrogen?

Hydrogen, like the first element in the periodic table, is small yet important.
We only make minimal modifcations, but those modifications are a large part of what makes tauOS special.

## Building

This will install Hydrogen to /usr/share/icons

```sh
$ meson build --prefix=/usr
$ cd build
$ sudo ninja install
```
