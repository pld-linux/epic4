%define help_version 4pre2.003
Summary:	Another popular Unix IRC client
Summary(pl):	Jeszcze jeden popularny Unixowy klient IRC
Name:		epic
Version:	4pre2.004
Release:	1
Copyright:	Distributable
Group:		Applications/Communications
Group(pl):	Aplikacje/Komunikacja
Source0:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-ALPHA/%{name}%{version}-19990618.tar.gz
Source1:	ftp://ftp.epicsol.org/pub/ircii/EPIC4-ALPHA/ircii-EPIC4pre2.003-help.tar.gz
Source2:	epic.wmconfig
URL:		http://www.epicsol.org/
Patch:		epic4-make.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
EPIC is the (E)nhanced (P)rogrammable (I)RC-II (C)lient.  It
is a program used to connect to IRC servers around the globe
so that the user can ``chat'' with others.

%description -l pl
EPIC to rozsz(E)rzony (P)rogramowalny kl(I)ent IR(C)-II. Jest
to program wykorzystywany do ³±czenia siê z serwerami IRC
na ca³ym ¶wiecie umo¿liwiaj±c porozumiewanie siê ze sob±.

%prep 
%setup -q -n ircii-EPIC%{version}
%patch0 -p1
gzip -dc %{SOURCE1} | tar -xf -

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
./configure --prefix=%{_prefix} \
	    --libexecdir=%{_bindir} \
	    --mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} \
     libexecdir=$RPM_BUILD_ROOT%{_bindir} install
cp -rp help $RPM_BUILD_ROOT%{_datadir}/epic
install -d  $RPM_BUILD_ROOT%{_mandir}/man1
install -d  $RPM_BUILD_ROOT/etc/X11/wmconfig
install     $RPM_SOURCE_DIR/epic.wmconfig    $RPM_BUILD_ROOT/etc/X11/wmconfig/epic

gzip -9nf   $RPM_BUILD_ROOT%{_mandir}/man1/* UPDATES KNOWNBUGS BUG_FORM doc/color.txt \
            doc/colors doc/TS4
find       $RPM_BUILD_ROOT%{_datadir}/epic -type f -exec gzip -9nf {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {UPDATES,KNOWNBUGS,BUG_FORM,doc/color.txt,doc/colors,doc/TS4}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/epic
%{_mandir}/man1/epic.*
/etc/X11/wmconfig/epic
