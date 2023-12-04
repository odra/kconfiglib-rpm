%global gittag 14.1.0

Name:           python3-kconfig
Version:        %{gittag}
Release:        1%{?dist}
Summary:        Kconfig implementation in Python.
License:        ISC
URL:            https://github.com/ulfalizer/Kconfiglib
Source:         https://github.com/ulfalizer/Kconfiglib/archive/refs/tags/v%{gittag}.tar.gz
 
BuildArch:      noarch

BuildRequires: python3-devel

%description
TODO

%prep
%autosetup -n Kconfiglib-%{version}

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

