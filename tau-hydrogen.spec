Summary:        Hydrogen Icon Theme for tauOS
Name:           tau-hydrogen
Version:        1.1
Release:        1%{dist}
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
* Thu Apr 21 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release