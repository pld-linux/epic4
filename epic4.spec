%define help_version 4pre2.003
Summary:	Another popular Unix IRC client
Summary(pl):	Jeszcze jeden popularny Unixowy klient IRC
Name:		epic
Version:	4.2000
Release:	1
Copyright:	Distributable
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-BETA/%{name}4-2000.tar.bz2
Source1:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-BETA/%{name}4pre2-help.tar.gz
Source2:	epic.desktop
Patch0:		epic4-2000-make.patch
Patch1:		epic-DESTDIR.patch
URL:		http://www.epicsol.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_bindir}

%description
EPIC is the (E)nhanced (P)rogrammable (I)RC-II (C)lient. It is a
program used to connect to IRC servers around the globe so that the
user can "chat" with others.

%description -l pl
EPIC to rozsz(E)rzony (P)rogramowalny kl(I)ent IR(C)-II. Jest to
program wykorzystywany do ³±czenia siê z serwerami IRC na ca³ym
¶wiecie umo¿liwiaj±c porozumiewanie siê z innymi.

%prep 
%setup -q -n epic4-2000
%patch0 -p1
%patch1 -p1

gzip -dc %{SOURCE1} | tar -xf -

%build
LDFLAGS=-s; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_mandir}/man1,%{_applnkdir}/Network/IRC}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rp help $RPM_BUILD_ROOT%{_datadir}/epic

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/IRC

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* UPDATES KNOWNBUGS BUG_FORM doc/color.txt \
	doc/colors doc/TS4

find $RPM_BUILD_ROOT%{_datadir}/epic -type f -exec gzip -9nf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {UPDATES,KNOWNBUGS,BUG_FORM,doc/color.txt,doc/colors,doc/TS4}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/epic
%{_mandir}/man1/epic.*
%{_applnkdir}/Network/IRC/*
