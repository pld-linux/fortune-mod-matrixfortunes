Summary:	Collection of Matrix Fortunes
Summary(pl):	Kolekcja fortunek z Matriksa
Name:		fortune-mod-matrixfortunes
Version:	0.1.0
Release:	10
License:	GPL
Group:		Applications/Games
Source0:	http://cx.capsi.com/src/matrixfortunes/matrixfortunes-%{version}.tar.bz2
# Source0-md5:	9a4cae06e21fb12a2e7a680053ec63c9
URL:		http://cx.capsi.com/code-matrixfortunes.html
Requires:	fortune-mod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

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
