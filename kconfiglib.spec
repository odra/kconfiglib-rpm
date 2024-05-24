Name:           kconfiglib
Version:        14.1.0
Release:        1%{?dist}
Summary:        Kconfig implementation in Python
License:        ISC
URL:            https://github.com/ulfalizer/Kconfiglib
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
Patch:          selftest.patch
 
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires: python3-kconfiglib

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

%install
%py3_install

sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/alldefconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/allmodconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/allnoconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/allyesconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/defconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/genconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/guiconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/listnewconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/menuconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/oldconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/olddefconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/savedefconfig.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/setconfig.py'

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
* Mon Dec 04 2023 Leonardo Rossetti <lrossett@redhat.com> - 14.1.0-1
- Initital spec file
