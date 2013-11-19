Summary:	Fast, simple object-to-object and broadcast signaling
Name:		python-blinker
Version:	1.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/b/blinker/blinker-%{version}.tar.gz
# Source0-md5:	66e9688f2d287593a0e698cd8a5fbc57
URL:		http://pythonhosted.org/blinker/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Blinker provides a fast dispatching system that allows any number
of interested parties to subscribe to events, or "signals".

%prep
%setup -qn blinker-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README
%{py_sitescriptdir}/blinker
%{py_sitescriptdir}/*.egg-info

