%define help_version 4pre2.003
Summary:	Another popular Unix IRC client
Summary(pl):	Jeszcze jeden popularny Unixowy klient IRC
Name:		epic4
Version:	1.0.1
Release:	1
License:	Distributable
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-PRODUCTION/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-BETA/%{name}pre2-help.tar.gz
Source2:	epic.desktop
Patch0:		epic-DESTDIR.patch
Patch1:		%{name}-gethostname_is_in_libc_aka_no_libnsl.patch
Patch2:		%{name}-config_file_path.patch
Patch3:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/%{name}-%{version}-ipv6-20010418.patch.gz
URL:		http://www.epicsol.org/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	epic

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
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	epicdir=%{_datadir}/epic

cp -rp help $RPM_BUILD_ROOT%{_datadir}/epic

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

gzip -9nf UPDATES KNOWNBUGS BUG_FORM doc/color.txt \
	doc/colors doc/TS4 doc/IP*

find $RPM_BUILD_ROOT%{_datadir}/epic -type f -exec gzip -9nf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/epic
%{_mandir}/man1/epic.*
%{_applnkdir}/Network/Communications/*
