#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-six
Version  : 1.16.0
Release  : 83
URL      : https://files.pythonhosted.org/packages/71/39/171f1c67cd00715f190ba0b100d606d440a28c93c7714febeca8b79af85e/six-1.16.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/71/39/171f1c67cd00715f190ba0b100d606d440a28c93c7714febeca8b79af85e/six-1.16.0.tar.gz
Summary  : Python 2 and 3 compatibility utilities
Group    : Development/Tools
License  : MIT
Requires: pypi-six-license = %{version}-%{release}
Requires: pypi-six-python = %{version}-%{release}
Requires: pypi-six-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-py
BuildRequires : pypi-pytest

%description
.. image:: https://img.shields.io/pypi/v/six.svg
:target: https://pypi.org/project/six/
:alt: six on PyPI

%package license
Summary: license components for the pypi-six package.
Group: Default

%description license
license components for the pypi-six package.


%package python
Summary: python components for the pypi-six package.
Group: Default
Requires: pypi-six-python3 = %{version}-%{release}

%description python
python components for the pypi-six package.


%package python3
Summary: python3 components for the pypi-six package.
Group: Default
Requires: python3-core
Provides: pypi(six)

%description python3
python3 components for the pypi-six package.


%prep
%setup -q -n six-1.16.0
cd %{_builddir}/six-1.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650558509
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test -v || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-six
cp %{_builddir}/six-1.16.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-six/ac6ba16d8833b691bbbda7c8eb0c06891c78f98f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-six/ac6ba16d8833b691bbbda7c8eb0c06891c78f98f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*