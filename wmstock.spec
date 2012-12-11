Summary:  A stock ticker in a small dock app
Name:		wmstock
Version: 0.11
Release: %mkrel 10
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
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%if %mdkversion < 200900
%post
%update_menus
%endif


%if %mdkversion < 200900
%postun
%clean_menus
%endif


%files
%defattr (-,root,root)
%doc CHANGES  COPYING  CREDITS  INSTALL  README  TODO
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.11-10mdv2010.0
+ Revision: 434897
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.11-9mdv2009.0
+ Revision: 262092
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.11-8mdv2009.0
+ Revision: 256263
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.11-6mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.11-6mdv2008.0
+ Revision: 87164
- fixed requires
- finer BuildRequires
- stop installing in old X11R6 path

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.11-5mdv2008.0
+ Revision: 69069
- convert menu entry to XDG
- use %%mkrel
- do not opencode spec-helper


* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.11-4mdk
- Rebuild

* Thu Jan 02 2003 HA Quôc-Viêt <viet@mandrakesoft.com> 0.11-3mdk
- minor spec cleanouts s/$RPM_BUILD_ROOT//tmp/wmstock-buildroot/g

* Tue Jul 31 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.11-2mdk
- Changed default Quotes to include MandrakeSoft, since our successful IPO
  yesterday :o) 
- compiled with the new libdockapp revision

* Thu Jul 26 2001 HA Quôc-Viêt <viet@mandrakesoft.com> 0.11-1mdk
- Initial packaging and release.

