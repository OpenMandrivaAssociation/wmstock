Summary:  A stock ticker in a small dock app
Name:		wmstock
Version: 0.11
Release: %mkrel 6
License:	GPL
Group:		Monitoring
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://mattfischer.com/wmstock/
Requires:	wget
BuildRequires:	libxpm-devel
BuildRequires:	libxext-devel
BuildRequires:	libxau-devel
BuildRequires:	libxdmcp-devel

%description
wmstock  is  a  stock  ticker  dock  app  for Window Maker.  It displays
stock quote data and cycles through tickers.  wmstock is designed to dock
with the Window Maker dock, but it will run as a 64x64 window an any window
manager.  wmstock is also very efficient with colors, and is 8-bit friendly.


%prep
rm -rf %buildroot

%setup -q -n wmstock

%build
make -C src CFLAGS="$RPM_OPT_FLAGS"

%install
[ -d %buildroot ] && rm -rf %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > %buildroot%{_liconsdir}/%{name}.png

mkdir -p %buildroot%{_bindir}
install -m 755 src/wmstock  %buildroot%{_bindir}
install -m 755 src/getquote %buildroot%{_bindir}

mkdir -p %buildroot%{_mandir}/man1
install -m644 src/wmstock.1x %buildroot%{_mandir}/man1/wmstock.1

install -m 755 -d %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=WmStock
Comment=A stock quote data display in a small icon
Exec=%{_bindir}/%{name} --delay=10 --open=8:30-16:00 --time2next=20 MAKE.PA INTC AMD
Icon=%{name}
Terminal=false
Type=Application
Categories=Office;Finance;
EOF


%clean
rm -rf %buildroot

%post
%update_menus


%postun
%clean_menus


%files
%defattr (-,root,root)
%doc CHANGES  COPYING  CREDITS  INSTALL  README  TODO
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*

