%define help_version 4pre2.003
Summary:	Another popular Unix IRC client
Summary(pl):	Jeszcze jeden popularny uniksowy klient IRC
Name:		epic4
Version:	1.2.9
Release:	4
License:	distributable
Group:		Applications/Communications
Source0:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-ALPHA/%{name}-%{version}.tar.bz2
# Source0-md5:	a5d13d53f7e1b4ad3103e25e4bbac5be
Source1:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-BETA/%{name}-help-20031208.tar.gz
# Source1-md5:	eec2c9ea0d4adccab0ba473080e15799
Source2:	epic.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gethostname_is_in_libc_aka_no_libnsl.patch
Patch2:		%{name}-config_file_path.patch
#Patch3:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/%{name}-%{version}-ipv6-20010418.patch.gz
#Patch4:		%{name}-ac.patch
Patch5:		http://linux.slupsk.net/patches/%{name}-maildir.patch
URL:		http://www.epicsol.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-devel
Requires:	perl(DynaLoader) = %(%{__perl} -MDynaLoader -e 'print DynaLoader->VERSION')
Conflicts:	lice <= 4.2.0-5
Obsoletes:	epic
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
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-ipv6
%{__make} epicdir=%{_datadir}/epic

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	epicdir=%{_datadir}/epic

cp -rp help $RPM_BUILD_ROOT%{_datadir}/epic

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc UPDATES KNOWNBUGS BUG_FORM doc/color.txt doc/colors doc/TS4 doc/EPIC*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/epic
%{_mandir}/man1/epic.*
%{_desktopdir}/*
