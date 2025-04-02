Name:           kconfiglib
Version:        14.1.0
Release:        3%{?dist}
Summary:        Kconfig implementation in Python
License:        ISC
URL:            https://github.com/zephyrproject-rtos/Kconfiglib
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch:          selftest.patch
 
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: help2man

%global _help2man() PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man --version-string='%{version}' --no-discard-stderr  --no-info --name=%1 --output=%{buildroot}%{_mandir}/man1/%1.1 %{buildroot}%{_bindir}/%1

%global _description %{expand:
Kconfiglib is a Kconfig implementation in Python 2/3. It started out as a
helper library, but now has a enough functionality to also work well as a
standalone Kconfig implementation (including terminal and GUI menuconfig
interfaces and Kconfig extensions).
}

%description %_description

%package -n python3-kconfiglib
Summary: Kconfig implementation in Python (library)

%description -n python3-kconfiglib
The kconfiglib's python library only sub-package.

%prep
%autosetup -n Kconfiglib-%{version}

%build
%py3_build

%check
cd ..
ln -s Kconfiglib-%{version} Kconfiglib
%{python3} Kconfiglib/testsuite.py
unlink Kconfiglib

%bcond_with bootstrap

%_help2man alldefconfig
%_help2man allmodconfig
%_help2man allnoconfig
%_help2man allyesconfig
%_help2man defconfig
%_help2man genconfig
%_help2man guiconfig
%_help2man listnewconfig
%_help2man menuconfig
%_help2man oldconfig
%_help2man olddefconfig
%_help2man savedefconfig
%_help2man setconfig

%install
%py3_install

%py3_shebang_fix '%{buildroot}%{python3_sitelib}/alldefconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/allmodconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/allnoconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/allyesconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/defconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/genconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/guiconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/listnewconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/menuconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/oldconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/olddefconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/savedefconfig.py'
%py3_shebang_fix '%{buildroot}%{python3_sitelib}/setconfig.py'

install -d '%{buildroot}%{_mandir}/man1'

%files
%doc README.rst
%license LICENSE.txt
%{_bindir}/alldefconfig
%{_bindir}/allmodconfig
%{_bindir}/allnoconfig
%{_bindir}/allyesconfig
%{_bindir}/defconfig
%{_bindir}/genconfig
%{_bindir}/guiconfig
%{_bindir}/listnewconfig
%{_bindir}/menuconfig
%{_bindir}/oldconfig
%{_bindir}/olddefconfig
%{_bindir}/savedefconfig
%{_bindir}/setconfig
%{_mandir}/man1/alldefconfig.1*
%{_mandir}/man1/allmodconfig.1*
%{_mandir}/man1/allnoconfig.1*
%{_mandir}/man1/allyesconfig.1*
%{_mandir}/man1/defconfig.1*
%{_mandir}/man1/genconfig.1*
%{_mandir}/man1/guiconfig.1*
%{_mandir}/man1/listnewconfig.1*
%{_mandir}/man1/menuconfig.1*
%{_mandir}/man1/oldconfig.1*
%{_mandir}/man1/olddefconfig.1*
%{_mandir}/man1/savedefconfig.1*
%{_mandir}/man1/setconfig.1*

%files -n python3-kconfiglib
%doc README.rst
%license LICENSE.txt
%pycached %{python3_sitelib}/alldefconfig.py
%pycached %{python3_sitelib}/allmodconfig.py
%pycached %{python3_sitelib}/allnoconfig.py
%pycached %{python3_sitelib}/allyesconfig.py
%pycached %{python3_sitelib}/defconfig.py
%pycached %{python3_sitelib}/genconfig.py
%pycached %{python3_sitelib}/guiconfig.py
%pycached %{python3_sitelib}/kconfiglib.py
%pycached %{python3_sitelib}/listnewconfig.py
%pycached %{python3_sitelib}/menuconfig.py
%pycached %{python3_sitelib}/oldconfig.py
%pycached %{python3_sitelib}/olddefconfig.py
%pycached %{python3_sitelib}/savedefconfig.py
%pycached %{python3_sitelib}/setconfig.py
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/PKG-INFO
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/PKG-INFO
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/SOURCES.txt
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/dependency_links.txt
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/entry_points.txt
%{python3_sitelib}/kconfiglib-%{version}-py%{python3_version}.egg-info/top_level.txt

%changelog
* Tues Apr 01 2025 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-4
- use built-in python macros

* Wed Mar 26 2025 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-3
- change to zenphyr repository org.

* Fri Sep 27 2024 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-2
- help2man support

* Mon Dec 04 2023 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-1
- Initital spec file
