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
%patch0 -p0

%build
export GECKO_LIBS="-rpath %{_libdir}/firefox-%{firefox_version}"
%configure2_5x --enable-gecko=firefox --disable-static
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang %name

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*

%post
%update_menus

%postun
%clean_menus
