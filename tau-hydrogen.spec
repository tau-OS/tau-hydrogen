Summary:        Hydrogen Icon Theme for tauOS
Name:           tau-hydrogen
Version:        1.1
Release:        10%{dist}
License:        GPLv3
URL:            https://tauos.co
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  ninja-build

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
