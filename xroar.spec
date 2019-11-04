Summary:	Dragon32, Dragon64 and Tandy CoCo emulator
Name:		xroar
Version:	0.35.4
Release:	1
License:	GPLv2+
Group:		Emulators
Url:		http://www.6809.org.uk/dragon/xroar.shtml
Source0:	http://www.6809.org.uk/dragon/%{name}-%{version}.tar.gz
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(sndfile)

%description
XRoar is a Dragon32, Dragon64 and Tandy CoCo emulator.
It uses standard cassette images (".cas" files) and virtual diskettes (".dsk"
or ".vdk" files) but has its own snapshot format at the moment (no ".pak" file
support).

%files
%doc ChangeLog COPYING* README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%dir %attr(0755,root,games) %{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export LDLIBS="-lm"
%configure
perl -pi -e "s#share#share/games#g" Makefile
%make_build

%install
#binary
mkdir -p %{buildroot}%{_gamesbindir}
install -m 755 src/%{name} %{buildroot}%{_gamesbindir}

#data dir
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}
#but is there some free software to put in there ?

#icons
install -d -m 755 %{buildroot}%{_miconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}%{_liconsdir}
install -m 644 %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

