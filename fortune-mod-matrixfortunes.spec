Summary:	Collection of Bofh Excuses Fortunes
Name:		fortune-mod-matrix-fortunes
Version:	0.1.0
Release:	10
Copyright:	GPL
Group:		Amusements/Games
Source0:	matrixfortunes-%{version}.tar.bz2
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's
your program. Fun-loving system administrators can add fortune to
users' .login files, so that the users get their dose of wisdom 
each time they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%prep
%setup -q -n matrixfortunes-%{version}
%build
%install
rm -rf $RPM_BUILD_ROOT

install -d		$RPM_BUILD_ROOT%{_datadir}/games/fortunes
install matrix*		$RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
