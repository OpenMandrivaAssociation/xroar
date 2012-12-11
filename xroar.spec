Name:		xroar
Version:	0.28.1
Release:	%mkrel 1
Summary:	Dragon32, Dragon64 and Tandy CoCo emulator
License:	GPLv2+
Group:		Emulators
URL:		http://www.6809.org.uk/dragon/xroar.shtml
Source0:	http://www.6809.org.uk/dragon/%{name}-%{version}.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	jackit-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	sndfile-devel
BuildRequires:	gtk2-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel

%description
XRoar is a Dragon32, Dragon64 and Tandy CoCo emulator.
It uses standard cassette images (".cas" files) and virtual diskettes (".dsk" 
or ".vdk" files) but has its own snapshot format at the moment (no ".pak" file 
support).

%prep
%setup -q -n %{name}-%{version}

%build
export LDLIBS="-lm"
%configure2_5x
perl -pi -e "s#share#share/games#g" Makefile
%make

%install
%__rm -rf %{buildroot}

#binary
%__mkdir_p %{buildroot}%{_gamesbindir}
%__install -m 755 %{name} %{buildroot}%{_gamesbindir}

#data dir
%__install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}
#but is there some free software to put in there ?

#icons
%__install -d -m 755 %{buildroot}/%{_miconsdir}
%__install -m 644 %{SOURCE1} %{buildroot}/%{_miconsdir}/%{name}.png
%__install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
%__install -d -m 755 %{buildroot}/%{_liconsdir}
%__install -m 644 %{SOURCE3} %{buildroot}/%{_liconsdir}/%{name}.png

#xdg menu
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=XRoar
Comment=Dragon32, Dragon64 and Tandy CoCo emulator
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;Game;GTK;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog COPYING* README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%dir %attr(0755,root,games) %{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png



%changelog
* Thu Jun 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.28.1-1mdv2012.0
+ Revision: 805558
- New version 0.28.1

* Fri May 25 2012 Andrey Bondrov <abondrov@mandriva.org> 0.28-1
+ Revision: 800650
- New version 0.28, spec cleanup

* Tue Aug 02 2011 Andrey Bondrov <abondrov@mandriva.org> 0.26-1
+ Revision: 692837
- imported package xroar


* Fri Dec  3 2010 Guillaume Bedot <littletux@zarb.org> 0.24-1plf2011.0
- 0.24

* Mon Jan  5 2009 Guillaume Bedot <littletux@zarb.org> 0.22-1plf2009.1
- 0.22

* Mon Apr 28 2008 Guillaume Bedot <littletux@zarb.org> 0.21-1plf2009.0
- 0.21
- icons as sources instead of br imagemagick

* Mon Mar  3 2008 Guillaume Bedot <littletux@zarb.org> 0.20-1plf2008.1
- 0.20
- fix buildrequires and desktop file

* Wed Jun 27 2007 Guillaume Bedot <littletux@zarb.org> 0.19-1plf2008.0
- 0.19

* Wed Mar 21 2007 Guillaume Bedot <littletux@zarb.org> 0.18-1plf2007.1
- Release 0.18
- Now use the configure script, some cleanups

* Wed Aug 30 2006 Anssi Hannula <anssi@zarb.org> 0.17-2plf2007.0
- fix buildrequires

* Mon Aug 21 2006 Guillaume Bedot <littletux@zarb.org> 0.17-1plf2007.0
- 0.17
- no more TODO

* Wed Aug  9 2006 Guillaume Bedot <littletux@zarb.org> 0.16-1plf2007.0
- 0.16
- updated doc
- fixed rights issue on doc and debug files

* Sat Jul 22 2006 Guillaume Bedot <littletux@zarb.org> 0.15-1plf2007.0
- First PLF package
