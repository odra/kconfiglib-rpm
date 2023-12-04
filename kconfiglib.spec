Name:           python3-kconfig
Version:        14.1.0
Release:        1
Summary:        Kconfig implementation in Python.
 
License:        ISC
URL:            https://github.com/ulfalizer/Kconfiglib
Source:         https://github.com/ulfalizer/Kconfiglib.git
 
BuildArch:      noarch

BuildRequires: python3-devel

%description
TODO

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%license LICENSE>txt
%{python3_sitelib}/kconfiglib/

%changelog
* Mon Dec 04 2023 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-1
- Initital spec file

