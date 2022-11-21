Summary:        Hydrogen Icon Theme for tauOS
Name:           tau-hydrogen
Version:        1.1
Release:        37%{dist}
License:        GPLv3
URL:            https://tauos.co
Source0:        https://github.com/tau-OS/tau-hydrogen/archive/refs/heads/main.zip
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  librsvg2-tools
BuildRequires:  xcursorgen

%description
Hydrogen is the default icon theme in tauOS.

%prep
%setup -q -n tau-hydrogen-main

%build
%meson
%meson_build

%install
# Install licenses
mkdir -p licenses
install -pm 0644 LICENSE licenses/LICENSE

%meson_install

%files
%license licenses/LICENSE
%doc README.md
%{_datadir}/icons/Hydrogen/*
%{_datadir}/gimp/2.0/palettes/Helium.gpl
%{_datadir}/inkscape/palettes/Helium.gpl

%changelog
* Wed May 18 2022 Lains <lainsce@airmail.cc> - 1.1-30
- All fullcolors

* Wed May 18 2022 Lains <lainsce@airmail.cc> - 1.1-29
- Almost all fullcolors

* Tue May 17 2022 Lains <lainsce@airmail.cc> - 1.1-28
- Missed some symbolic refinements, did them

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-27
- Folders go Gluon Brown, Documents Folder goes blue

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-26
- Final symbolic refinements

* Mon May 9 2022 Lains <lainsce@airmail.cc> - 1.1-25
- Use HIG colors

* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-24
- Fix meson bruh moment

* Sun May 8 2022 Lains <lainsce@airmail.cc> - 1.1-23
- Fix meson bruh moment

* Sat May 7 2022 Lains <lainsce@airmail.cc> - 1.1-22
- Finish cursor theme

* Fri May 6 2022 Lains <lainsce@airmail.cc> - 1.1-21
- Finish symbolics

* Thu May 5 2022 Lains <lainsce@airmail.cc> - 1.1-20
- More symbolics, and more refinements

* Wed May 4 2022 Lains <lainsce@airmail.cc> - 1.1-19
- Make cursors more visible in dark bg, still wasn't enough

* Tue May 3 2022 Lains <lainsce@airmail.cc> - 1.1-18
- Make cursors more visible in dark bg

* Tue May 3 2022 Lains <lainsce@airmail.cc> - 1.1-17
- Make cursors visible in dark bg

* Tue May 3 2022 Lains <lainsce@airmail.cc> - 1.1-16
- More icons, install cursor to proper place

* Mon May 2 2022 Lains <lainsce@airmail.cc> - 1.1-15
- Cursor theme

* Sun May 1 2022 Lains <lainsce@airmail.cc> - 1.1-14
- 1px stroke symbolics, defining the Hydrogen Design System

* Sun May 1 2022 Lains <lainsce@airmail.cc> - 1.1-13
- More symbolics, and more refinements

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-12
- Audio symbolics, and some refinements

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-11
- Wireless symbolics, and some refinements

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-10
- More refinement in many icons

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-9
- Window control symbolics

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-8
- More refinements and symbolics

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-7
- More refinement

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-6
- More symbolics and refinement

* Thu Apr 28 2022 Lains <lainsce@airmail.cc> - 1.1-5
- Refinement of status symbolics

* Wed Apr 27 2022 Lains <lainsce@airmail.cc> - 1.1-4
- Arrival of status symbolics, and Builder

* Wed Apr 27 2022 Lains <lainsce@airmail.cc> - 1.1-3
- More symbolics

* Tue Apr 26 2022 Lains <lainsce@airmail.cc> - 1.1-2
- All core and utilities apps icons done

* Thu Apr 21 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
