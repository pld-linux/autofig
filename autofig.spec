Summary:	Automatic *-config scripts generation
Summary(pl):	Automatyczne generowanie skryptów *-config
Name:		autofig
Version:	0.1
Release:	1
License:	?
Group:		Development/Tools
# origins from GNOME CVS?
Source0:	http://autotrace.sourceforge.net/tools/%{name}.tar.gz
# Source0-md5:	864f4729560bdc2c0eabfd3857a557e2
BuildRequires:	autoconf
Requires:	m4
Requires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for automatic *-config scripts generation.

%description -l pl
Narzêdzie do automatycznego generowanie skryptów *-config.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f samples/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog doc samples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
