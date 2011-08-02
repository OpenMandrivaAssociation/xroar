Name:			xroar
Version:		0.26
Release:		%mkrel 1

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
BuildRequires:	alsa-lib-devel
BuildRequires:	sndfile-devel
BuildRequires:	gtk2-devel
%if %mdkversion >= 200700
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
%else
BuildRequires:	X11-devel
BuildRequires:	MesaGLU-devel
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
XRoar is a Dragon32, Dragon64 and Tandy CoCo emulator.
It uses standard cassette images (".cas" files) and virtual diskettes (".dsk" 
or ".vdk" files) but has its own snapshot format at the moment (no ".pak" file 
support).

%prep

%setup -q -n %{name}-%{version}
%configure2_5x
perl -pi -e "s#share#share/games#g" Makefile

%build
make

%install
rm -rf %{buildroot}

#binary
mkdir -p %{buildroot}%{_gamesbindir}
install -m 755 %{name} %{buildroot}%{_gamesbindir}

#data dir
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{name}
#but is there some free software to put in there ?

#icons
install -d -m 755 %{buildroot}/%{_miconsdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_miconsdir}/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
install -d -m 755 %{buildroot}/%{_liconsdir}
install -m 644 %{SOURCE3} %{buildroot}/%{_liconsdir}/%{name}.png

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

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING* README
%attr(0755,root,games) %{_gamesbindir}/%{name}
%dir %attr(0755,root,games) %{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

