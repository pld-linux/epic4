Summary:	Another popular Unix IRC client
Summary(pl.UTF-8):	Jeszcze jeden popularny uniksowy klient IRC
Name:		epic4
Version:	2.10.11
Release:	1
License:	distributable
Group:		Applications/Communications
Source0:	https://ftp.epicsol.org/pub/epic/EPIC4-PRODUCTION/%{name}-%{version}.tar.xz
# Source0-md5:	2961e927461aab76352af7128c8aea67
Source1:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-PRODUCTION/%{name}-help-20050315.tar.gz
# Source1-md5:	9888d1af465ca72bf9a02487264071a5
Source2:	epic.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gethostname_is_in_libc_aka_no_libnsl.patch
Patch2:		%{name}-config_file_path.patch
Patch3:		type-checks.patch
URL:		http://www.epicsol.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	perl-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	lice <= 4.2.0-5
Obsoletes:	epic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EPIC is the (E)nhanced (P)rogrammable (I)RC-II (C)lient. It is a
program used to connect to IRC servers around the globe so that the
user can "chat" with others.

%description -l pl.UTF-8
EPIC to rozsz(E)rzony (P)rogramowalny kl(I)ent IR(C)-II. Jest to
program wykorzystywany do łączenia się z serwerami IRC na całym
świecie umożliwiając porozumiewanie się z innymi.

%prep
%setup -q -a 1
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-ipv6 \
	--with-perl
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
%attr(755,root,root) %{_bindir}/epic
%attr(755,root,root) %{_bindir}/epic-EPIC4*
%dir %{_libexecdir}/epic
%attr(755,root,root) %{_libexecdir}/epic/wserv4
%{_datadir}/epic
%{_mandir}/man1/epic.*
%{_desktopdir}/*.desktop
