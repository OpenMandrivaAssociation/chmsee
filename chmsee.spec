Name: chmsee
Version: 1.0.0
Release: %mkrel 1
Summary: A Gtk+2 based CHM viewer
License: GPL
URL: http://chmsee.gro.clinux.org/
Group: Graphical desktop/GNOME
Source: http://gro.clinux.org/frs/download.php/2040/%{name}-%{version}.tar.gz
BuildRequires: libglade2.0-devel
BuildRequires: mozilla-firefox-devel
BuildRequires: openssl-devel
BuildRequires: chmlib-devel
BuildRequires: intltool

%description
ChmSee is an HTML Help viewer for Unix/Linux. It is based on CHMLIB
and use Gtk2+ as frontend toolkit. Because of using gecko as HTML
rendering engine, ChmSee can support rich features of modern HTML
page, such as CSS and JavaScript.

%prep
%setup -q

%build
%configure2_5x
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
