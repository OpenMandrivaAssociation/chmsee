%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom
%define xulrunner 1.9
%define xullibname %mklibname xulrunner %xulrunner
%define xulver %(rpm -q --queryformat %%{VERSION} %xullibname)

Name: chmsee
Version: 1.0.2
Release: %mkrel 1
Summary: A Gtk+2 based CHM viewer
License: GPLv2+
URL: http://code.google.com/p/chmsee/
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://chmsee.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1: chmsee-1.0.2-desktop-icon.patch
Patch2: chmsee-1.0.1-fix-str-fmt.patch
BuildRequires: libglade2.0-devel
BuildRequires: xulrunner-devel-unstable
BuildRequires: openssl-devel
BuildRequires: libgcrypt-devel
BuildRequires: chmlib-devel
BuildRequires: intltool
BuildRequires: imagemagick
Requires: %xullibname = %xulver

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use Gtk2+ as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q
%patch1 -p0
%patch2 -p0

%build
%configure2_5x --with-gecko=libxul
%make

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

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%clean_mime_database
%endif
