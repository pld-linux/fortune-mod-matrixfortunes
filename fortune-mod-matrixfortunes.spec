Summary:	Collection of Matrix Fortunes
Summary(pl.UTF-8):	Kolekcja fortunek z Matriksa
Name:		fortune-mod-matrixfortunes
Version:	0.1.0
Release:	10
License:	GPL
Group:		Applications/Games
Source0:	http://cx.capsi.com/src/matrixfortunes/matrixfortunes-%{version}.tar.bz2
# Source0-md5:	9a4cae06e21fb12a2e7a680053ec63c9
URL:		http://cx.capsi.com/code-matrixfortunes.html
Requires:	fortune-mod
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

%prep
%setup -q -n matrixfortunes-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install matrix* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
