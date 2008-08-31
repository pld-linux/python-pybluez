%define 	realname 	pybluez
#
Summary:	Python modules for wrappers around system Bluetooth resources
Summary(pl.UTF-8):	Moduły Pythona do obsługi urządzeń Bluetooth
Name:		python-%{realname}
Version:	0.9.2
Release:	2
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://org.csail.mit.edu/pybluez/release/%{realname}-src-%{version}.tar.gz
# Source0-md5:	49c8bdd5d8def11df40ce3a84b7ab839
Url:		http://org.csail.mit.edu/pybluez/
BuildRequires:	bluez-libs-devel
BuildRequires:	pydoc
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pybluez contains Python modules for wrappers around system
Bluetooth resources.

%description -l pl.UTF-8
Pakiet pybluez zawiera moduły Pythona do obsługi urządzeń Bluetooth.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__python} setup.py build

%install
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
./doc/gendoc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README doc/*.html
%attr(755,root,root) %{py_sitedir}/_bluetooth.so
%{py_sitedir}/bluetooth.py[co]
%{py_sitedir}/PyBluez-*.egg-info
%{_examplesdir}/%{name}-%{version}
