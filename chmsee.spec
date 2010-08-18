%define _requires_exceptions libnspr4\\|libplc4\\|libplds4\\|libnss\\|libsmime3\\|libsoftokn\\|libssl3\\|libgtkembedmoz\\|libxpcom

Name: chmsee
Version: 1.2.0
Release: %mkrel 1
Summary: A Gtk+2 based CHM viewer
License: GPLv2+
URL: http://code.google.com/p/chmsee/
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://chmsee.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libglade2.0-devel
%if %mdvver >= 201000
BuildRequires:	xulrunner-devel
%else
BuildRequires:	xulrunner-devel-unstable
%endif
BuildRequires: openssl-devel
BuildRequires: libgcrypt-devel
BuildRequires: chmlib-devel
BuildRequires: intltool
BuildRequires: imagemagick
BuildRequires: cmake
BuildRequires: libxml2-devel
%if %mdvver >= 201000
Requires: libxulrunner = %{xulrunner_version}
%else
#gw as Fedora does:
%define xulrunner 1.9
%define libname %mklibname xulrunner %xulrunner
%define xulver %(rpm -q --queryformat %%{VERSION} %libname)
Requires: %libname = %xulver
%endif


%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use Gtk2+ as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q

%build
%cmake 
%make

%install
%__rm -rf %buildroot
pushd build
%makeinstall_std
popd

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -p -m 644 -D data/chmsee-icon.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/chmsee.png
convert data/chmsee-icon.png -resize 16x16 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/chmsee.png
convert data/chmsee-icon.png -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/chmsee.png

%find_lang %name

%clean
%__rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/chmsee
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/*/*
