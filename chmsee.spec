%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define firefox_version %(rpm -q mozilla-firefox --queryformat %{VERSION})

Name: chmsee
Version: 1.0.0
Release: %mkrel 1
Summary: A Gtk+2 based CHM viewer
License: GPL
URL: http://chmsee.gro.clinux.org/
Group: Graphical desktop/GNOME
Source: http://gro.clinux.org/frs/download.php/2040/%{name}-%{version}.tar.gz
Patch0: chmsee-1.0.0-add-gecko-root.patch
Patch1: chmsee-1.0.0-desktop-icon.patch
BuildRequires: libglade2.0-devel
BuildRequires: mozilla-firefox-devel
BuildRequires: openssl-devel
BuildRequires: chmlib-devel
BuildRequires: intltool
Requires: %mklibname mozilla-firefox %firefox_version

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use Gtk2+ as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q
%patch0 -p0 -b .gecko
%patch1 -p1

%build
./autogen.sh
%configure2_5x --enable-gecko=firefox --disable-static
cd src
make
cd -
cd po
make
cd -
intltool-merge -d -u -c ./po/.intltool-merge-cache ./po chmsee.desktop.in chmsee.desktop

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -p -m 644 -D chmsee-icon.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/chmsee.png
convert chmsee-icon.png -resize 16x16 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/chmsee.png
convert chmsee-icon.png -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/chmsee.png

%find_lang %name

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/chmsee
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*.png

%post
%update_menus

%postun
%clean_menus
