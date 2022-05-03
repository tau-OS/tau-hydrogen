Summary:        Hydrogen Icon Theme for tauOS
Name:           tau-hydrogen
Version:        1.1
Release:        15%{dist}
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  librsvg-tools
BuildRequires:  xcursorgen

%description
Hydrogen is the default icon theme in tauOS.

%prep
%autosetup

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

%changelog
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
